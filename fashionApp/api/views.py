from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class VideoPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'videos': data,
            'pagination': {
                'page': self.page.number,
                'limit': self.page_size,
                'total_pages': self.page.paginator.num_pages,
                'total_videos': self.page.paginator.count,
                'next_cursor': self.get_next_link(),
            }
        })

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().select_related('user', 'music').prefetch_related('products__store', 'products__variants')
    serializer_class = VideoSerializer
    pagination_class = VideoPagination
