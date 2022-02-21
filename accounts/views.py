from django.shortcuts import render


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')