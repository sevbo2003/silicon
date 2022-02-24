from django.contrib import admin
from .models import Category, Tags, Post, Comments

admin.site.register(Category)
admin.site.register(Tags)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'hot_post', 'created_at', 'category', 'number_of_likes')
    list_filter = ('created_at', 'hot_post', 'author', 'category')
    search_fields = ('title', 'author', 'tags')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    list_display = ('comment', 'created_at', 'user')
    search_fields = ('comment',)
    