from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Subscriber, CustomUser
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone', 'bio')

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    bio = forms.CharField(max_length=500, required=False)

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if phone[1:].isdigit():
    #         return str(phone)
    #     else:
    #         raise ValidationError('That is not number')


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg rounded-3 ps-5',
        'type': 'email',
        'placeholder': 'Your email'
    }), label='')
