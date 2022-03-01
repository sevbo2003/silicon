from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Category, Tags, Comments
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
from accounts.models import Subscriber
from accounts.forms import SubscriberForm
from django.core.mail import send_mail
from datetime import datetime
from django.conf import settings
from .forms import CommentForm, ContactForm
from accounts.models import CustomUser, Contact
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required



@login_required
def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    path = f"{post.get_absolute_url()}#share-post"
    return HttpResponseRedirect(path)


@login_required
def save_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.savers.add(request.user)
    return HttpResponseRedirect(reverse('account_saves'))


@login_required
def save_remove_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.savers.remove(request.user)
    return HttpResponseRedirect(reverse('account_saves'))


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
                send_mail('Subscriptions', 'You successfully subscribed to our newsletter. Thanks)',
                          'sevbofx@gmail.com', (email,))
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
    numbers = Post.objects.all().count()
    context = {
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'tags': tags,
        'numbers': numbers
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
            p = Comments(comment=comment, post=post, user=request.user, created_at=datetime)
            p.save()
            path = f"{post.get_absolute_url()}#comment-section"
            return HttpResponseRedirect(path)
    else:
        comment_form = CommentForm()
    print(request.session.session_key)
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


def category_posts(request, category):
    category = get_object_or_404(Category, category=category)
    categories = Category.objects.all()
    tags = Tags.objects.all()[:6]
    top_posts = Post.objects.annotate(num=Count('likes')).order_by('-num')[:3]
    query = request.GET.get('search')
    if query:
        posts = Post.objects.filter(category=category).filter(
            Q(title__icontains=query) | Q(description__icontains=query))
    else:
        posts = Post.objects.filter(category=category)
    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts, 6)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    numbers = Post.objects.all().count()
    page_cat = str(category.category)
    print(page_cat)
    context = {
        'cat_post': category,
        'posts': posts,
        'top_posts': top_posts,
        'categories': categories,
        'tags': tags,
        'numbers': numbers,
        'page_cat': page_cat
    }
    return render(request, 'category_posts.html', context)


def account_saves(request):
    posts = Post.objects.filter(savers=request.user)
    return render(request, 'account-saved-items.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone = contact_form.cleaned_data['phone']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            p = Contact(name=name, email=email, subject=subject, phone=phone, message=message, created_at=datetime)
            p.save()
            send_mail(subject, message, 'sevbofx@gmail.com', [email])
    else:
        contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})
