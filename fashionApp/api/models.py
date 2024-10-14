from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    profile_picture_url = models.URLField()
    bio = models.TextField()
    followers_count = models.IntegerField()
    verified = models.BooleanField(default=False)

class Store(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField()
    image_url = models.URLField()
    timestamp = models.IntegerField()
    currency = models.CharField(max_length=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)

class Variant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    options = models.JSONField()

class Music(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    cover_url = models.URLField()

class Video(models.Model):
    video_url = models.URLField()
    thumbnail_url = models.URLField()
    description = models.TextField()
    view_count = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    likes_count = models.IntegerField()
    comments_count = models.IntegerField()
    shares_count = models.IntegerField()
    is_liked = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    hashtags = models.JSONField()
