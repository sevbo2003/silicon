from django.urls import path
from .views import homepage, post_detail, post_list, account_details, like_view


urlpatterns = [
    path('', homepage, name='home'),
    path('post-list/', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('accounts/details/', account_details, name='account-details'),
    path('like/<int:pk>/', like_view, name='like_post')
]