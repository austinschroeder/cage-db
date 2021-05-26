from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gifs/', views.gifs, name='gifs'),
    path('movies/', views.movies_index, name='index'),
    path('movies/new/', views.create_movie, name='create_movie'),
    path('movies/<int:movie_id>/', views.detail, name='detail'),
    path('movies/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('movies/<int:movie_id>/edit/', views.update_movie, name='update_movie'),
]

# Steps to create a new page
# 1. Create the path in urls.py
# 2. Create a view function
# 3. Create the template for the page