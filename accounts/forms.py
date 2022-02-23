from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Subscriber
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg rounded-3 ps-5',
        'type': 'email',
        'placeholder': 'Your email'
    }), label='')