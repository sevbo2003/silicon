from django.urls import path
from .views import PostApiView


urlpatterns = [
    path('posts/', PostApiView.as_view())
]