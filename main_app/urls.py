from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gifs/', views.gifs, name='gifs'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movie_id>/', views.detail, name='detail'),
]

# Steps to create a new page
# 1. Create the path in urls.py
# 2. Create a view function
# 3. Create the template for the page