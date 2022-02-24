from django.urls import path
from .views import homepage, post_detail, post_list


urlpatterns = [
    path('', homepage, name='home'),
    path('post-list/', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
]