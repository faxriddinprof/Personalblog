from django.urls import path
from .views import GetPosts, GetPost, GetPostsbyTag, about

urlpatterns = [
    path('', GetPosts, name='post_all'),
    path('detail/<int:pk>/', GetPost, name='post_detail'),
    path('filter/<str:tagName>', GetPostsbyTag, name='post_filter'),
    path('about/', about, name='about')
]
