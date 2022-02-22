from django.shortcuts import render, redirect, reverse
# from .models import Post, Category, Tags


def homepage(request):
    # hot = Post.objects.get(hot_post=True)
    # posts = Post.objects.all()
    # categories = Category.objects.all()
    # context = {
    #     'hot': hot,
    #     'posts': posts,
    #     'categories': categories
    # }
    return render(request, 'home.html')

