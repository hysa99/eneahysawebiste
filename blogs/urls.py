
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



app_name = 'blogs'


urlpatterns = [
    path('', views.blog_home, name='blogs'),
    path('<int:pk>/', views.details, name='details'),
    path('blogs/like/<int:pk>', views.like_post, name='like_post'),
]
