from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gifs(request):
  return render(request, 'gifs.html')

def movies_index(request):
  #Retrieve all movies from DB
  movies = Movie.objects.all() #[]

  context = { 'movies': movies }
  #Retrieve a template
  #Combine the data with the template and send HTML back to browser
  return render(request, 'movies/movies-index.html', context)

def detail(request, movie_id):
  #get the movie data for a certain movie by its ID
  found_movie = Movie.objects.get(id=movie_id)

  
  context = { 'movie': found_movie }

  return render(request, 'movies/movies-detail.html', context)