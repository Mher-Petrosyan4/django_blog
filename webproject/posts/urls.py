from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path("", views.home, name='homepage'),
    path('create-post/', views.create_post, name='create-post'),
    path('profile/', views.user_posts, name='user-posts'),
    path('like/', views.like_post, name='like-post'),
]