from rest_framework import serializers
from blog.models import Post
from accounts.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'tags', 'created_at', 'hot_post',)

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        data['category'] = instance.category.category
        data['author'] = instance.author.username
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'image', 'bio', 'is_staff')
