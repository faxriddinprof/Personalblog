from django.urls import path
from .views import GetPosts, GetPost

urlpatterns = [
    path('', GetPosts, name='post_all'),
    path('detail/<int:pk>/', GetPost, name='post_detail'),
]
