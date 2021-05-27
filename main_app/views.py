from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gifs(request):
  return render(request, 'gifs.html')

#+=+=+ INDEX +=+=+
@login_required
def movies_index(request):
  #Retrieve all movies from DB
  # movies = Movie.objects.filter(user=request.user).order_by('-year')
  movies = Movie.objects.order_by('-year')

  context = { 'movies': movies }
  #Retrieve a template
  #Combine the data with the template and send HTML back to browser
  return render(request, 'movies/movies-index.html', context)

def detail(request, movie_id):
  #get the movie data for a certain movie by its ID
  found_movie = Movie.objects.get(id=movie_id)

  
  context = { 'movie': found_movie }

  return render(request, 'movies/movies-detail.html', context)

#==CREATE==
def create_movie(request):
  if request.method == 'GET':
  #Create a movie form
    form = MovieForm()
    #create context
    context = {
      'form': form
    }
  #Respond with new movie template and form
    return render(request, 'movies/movies-new.html', context)
  
  else:
    # Use MovieForm to get data from request
    # MovieForm will also make sure the data matches Movie Model
    form = MovieForm(request.POST, request.FILES)
    if form.is_valid():
      movie = form.save(commit=False)
      movie.user = request.user
      movie.save()
      #Redirect to Movie detail template
      return redirect('detail', movie.id)



#==DELETE==
def delete_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  movie.delete()
  return redirect('index')

#==UPDATE==
def update_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)

  if request.method == 'GET':
    #Send the MovieForm
    form = MovieForm(instance=movie)
    context = {
      'form': form
    }

    return render(request, 'movies/movies-edit.html', context)
  else:
    # Handle update form
    form = MovieForm(request.POST, request.FILES, instance=movie)
    if form.is_valid():
      movie = form.save()
      return redirect('detail', movie.id)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#===SIGNUP===
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # Auto-login
      login(request, user)
      return redirect('index')
    else:
      #send error msg to user
      error_message = 'Password or Username is invalid'

  form = UserCreationForm()

  context = {
    'form': form,
    'error_message': error_message
  }

  return render(request, 'registration/signup.html', context)

# testing