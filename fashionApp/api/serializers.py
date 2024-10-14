from rest_framework import serializers
from .models import Video, User, Product, Store, Variant, Music

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    variants = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductSerializer(many=True)
    music = MusicSerializer()

    class Meta:
        model = Video
        fields = '__all__'
