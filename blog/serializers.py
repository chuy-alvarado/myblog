from rest_framework import serializers
from .models import Post
from django.utils import timezone

class PostSerializer(serializers.ModelSerializer):
    publish_date = serializers.DateField(default=timezone.now, read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'publish_date', 'created_by', 'featured']