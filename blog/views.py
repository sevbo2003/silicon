from django.shortcuts import render, redirect, reverse
from .models import Post, Category, Tags
from django.db.models import Q, Count


def homepage(request):
    hot = Post.objects.filter(hot_post=True)[0]
    cat_posts = []
    for cat in Category.objects.all():
        try:
            cat_posts.append(Post.objects.filter(category=cat)[0])
        except:
            pass
    top_posts = Post.objects.annotate(num=Count('likes')).order_by('-num')[:6]
    posts = Post.objects.all()[:6]
    categories = Category.objects.all()
    context = {
        'hot': hot,
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'cat_posts': cat_posts[::-1]
    }
    return render(request, 'home.html', context)

