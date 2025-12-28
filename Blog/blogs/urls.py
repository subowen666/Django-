"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new post.
    path('new/', views.new_post, name='new_post'),
    # Page for editing a post.
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    # Page for user's posts.
    path('user/<str:username>/', views.user_posts, name='user_posts'),
]