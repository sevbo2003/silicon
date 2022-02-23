from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category, Tags
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from accounts.models import Subscriber
from accounts.forms import SubscriberForm
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings


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
    if request.method == 'POST':
        email_form = SubscriberForm(request.POST)
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                pass
            else:
                p = Subscriber(email=email, joined=datetime)
                p.save()
                send_mail('Subscriptions', 'You successfully subscribed to our newsletter. Thanks)', 'sevbofx@gmail.com', (email,))
                path = f"{request.META.get('HTTP_REFERER')}#footer1"
                return HttpResponseRedirect(path)
    else:
        email_form = SubscriberForm()
    context = {
        'hot': hot,
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'cat_posts': cat_posts[::-1],
    }
    return render(request, 'home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    releated_arts = Post.objects.filter(category=post.category)[:3]
    context = {
        'post': post,
        'releated_arts': releated_arts
    }
    return render(request, 'blog-single.html', context)

