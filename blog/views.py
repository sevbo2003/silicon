from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category, Tags, Comments
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from accounts.models import Subscriber
from accounts.forms import SubscriberForm
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings
from .forms import CommentForm
from accounts.models import CustomUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def post_list(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()[:6]
    top_posts = Post.objects.annotate(num=Count('likes')).order_by('-num')[:3]
    query = request.GET.get('search')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        posts = Post.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    releated_arts = Post.objects.filter(category=post.category)[:3]
    # print(request.user.first_name == '')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data.get('comment')
            p = Comments(comment=comment, post=post,user=request.user ,created_at=datetime)
            p.save()
            path = f"{post.get_absolute_url()}#comment-section"
            return HttpResponseRedirect(path)
    else:
        comment_form = CommentForm()
    comments = post.comments.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(comments, 8)
    try:
        comments = paginator.page(page_num)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    context = {
        'post': post,
        'releated_arts': releated_arts,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'post_detail.html', context)

