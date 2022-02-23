from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Subscriber

from .forms import UserChangeForm, UserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'joined')
    list_filter = ('joined',)
    search_fields = ('email',)
