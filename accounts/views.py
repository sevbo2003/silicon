from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def account_details(request):
    if request.method == 'POST':
        user_update = CustomUserUpdateForm(request.POST)
        if user_update.is_valid():
            user = CustomUser.objects.get(username=request.user.username)
            if request.user.first_name:
                name = request.user.first_name
            else:
                name = user_update.cleaned_data['first_name']
            if request.user.last_name != '':
                surname = request.user.last_name
            else:
                surname = user_update.cleaned_data['last_name']
            if request.user.phone != '':
                phone = request.user.phone
            else:
                phone = user_update.cleaned_data['phone']
            if request.user.bio != '':
                bio = request.user.bio
            else:
                bio = user_update.cleaned_data['bio']
            user.phone = phone
            user.bio = bio
            user.first_name = name
            user.last_name = surname
            user.save()
            return redirect('account-details')
    else:
        user_update = CustomUserUpdateForm()
    return render(request, 'account-details.html', {'user_update': user_update})