from django.urls import path
from .views import homepage, post_detail


urlpatterns = [
    path('', homepage, name='home'),
    path('post/<str:slug>/', post_detail, name='post_detail')
]