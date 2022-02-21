from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')