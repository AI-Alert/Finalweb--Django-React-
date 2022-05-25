from rest_framework import serializers
from vollclub.models import Post, Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')