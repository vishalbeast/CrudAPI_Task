"""Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #create
    path('users/', views.create_user, name='create_user'),
    path('posts/', views.create_post, name='create_post'),
    path('likes/', views.create_like, name='create_like'),
    #Read
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('posts/<int:post_id>/', views.get_post, name='get_post'),
    path('likes/<int:like_id>/', views.get_like, name='get_like'),
    path('posts/', views.get_all_posts, name='get_all_posts'),
    # Update
    path('users/<int:user_id>/', views.update_user, name='update_user'),
    path('posts/<int:post_id>/', views.update_post, name='update_post'),
    path('likes/<int:like_id>/', views.update_like, name='update_like'),
    # Delete 
    path('users/<int:user_id>/', views.delete_user, name='delete_user'),
    path('posts/<int:post_id>/', views.delete_post, name='delete_post'),
    path('likes/<int:like_id>/', views.delete_like, name='delete_like'),
]
