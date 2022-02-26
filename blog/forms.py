from django import forms
from .models import Comments
from accounts.models import Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')
