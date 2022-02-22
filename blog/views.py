from django.shortcuts import render, redirect, reverse


def homepage(request):
    return render(request, 'home.html', {})


