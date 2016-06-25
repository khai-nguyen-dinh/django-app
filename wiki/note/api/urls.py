from django.conf.urls import url
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostDeletelAPIView,
    PostUpdatelAPIView,
    PostCreateAPIView,
    UserListAPIView
)

urlpatterns = [
    url(r'^/post/$', PostListAPIView.as_view(), name='post_list'),
    url(r'^/user/$', UserListAPIView.as_view(), name='user_list'),
    url(r'^/create/$', PostCreateAPIView.as_view(), name='post_detail'),
    url(r'^/(?P<pk>[\w-]+)/detail/$', PostDetailAPIView.as_view(), name='post_create'),
    url(r'^/(?P<pk>[\w-]+)/delete/$', PostDeletelAPIView.as_view(), name='post_delete'),
    url(r'^/(?P<pk>[\w-]+)/update/$', PostUpdatelAPIView.as_view(), name='post_update'),
]
