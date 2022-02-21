from django.urls import path
from .views import homepage
from accounts.views import signup, signin


urlpatterns = [
    path('', homepage, name='home'),
    path('sign-up/', signup, name='sign-up'),
    path('sign-in/', signin, name='sign-in'),
]