from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CustomUser


class Category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Tags(models.Model):
    tag = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='posts/thumbnails')
    image = models.ImageField(upload_to='posts/images')
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='likes')
    savers = models.ManyToManyField(CustomUser, blank=True, related_name='savers')
    hot_post = models.BooleanField(default=False)
    slug = models.SlugField()

    def get_absolute_url(self):
        return f"/post/{self.slug}/"

    class Meta:
        ordering = ('-created_at',)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return self.comment
