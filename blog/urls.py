from django.urls import path, include
from .views import homepage, post_detail, post_list, like_view, category_posts, account_saves, \
    save_view, save_remove_view, contact, PostViewSet, UserViewSet
from accounts.views import account_details
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', homepage, name='home'),
    path('post-list/', post_list, name='post_list'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('accounts/details/', account_details, name='account-details'),
    path('accounts/saves/', account_saves, name='account_saves'),
    path('like/<int:pk>/', like_view, name='like_post'),
    path('save/<int:pk>/', save_view, name='save_post'),
    path('remove/<int:pk>/', save_remove_view, name='remove_post'),
    path('category/<str:category>/', category_posts, name='category_posts'),
    path('contact/', contact, name='contact'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
