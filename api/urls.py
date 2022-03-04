from django.urls import path
from .views import PostApiView, UserApiView


urlpatterns = [
    path('posts/', PostApiView.as_view()),
    path('users/', UserApiView.as_view()),
]