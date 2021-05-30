from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm, UserFeedbackForm
# from .forms import PhotoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Movie, UserFeedback 
# from .models import Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cage-db-bucket'


def home(request):
  return render(request, 'home.html')
#=============================================================
def about(request):
  return render(request, 'about.html')
#=============================================================
def gifs(request):
  return render(request, 'gifs.html')
#=============================================================
def add_review(request, movie_id):
  form = UserFeedbackForm(request.POST)
  if form.is_valid():
    new_review=form.save(commit=False)
    new_review.movie_id = movie_id
    new_review.save()
    return redirect('detail', movie_id)

#=============================================================

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

#=============================================================


def detail(request, movie_id):
  #get the movie data for a certain movie by its ID
  found_movie = Movie.objects.get(id=movie_id)
  print(found_movie.userfeedback_set.all())

  user_review = UserFeedbackForm()
  
  context = { 'movie': found_movie,
              'form': user_review,

  }

  return render(request, 'movies/movies-detail.html', context)

#=============================================================
#==CREATE==
def create_movie(request):
  if request.method == 'GET':
  #Create a movie form
    form = MovieForm()
    #create context
    context = {
      'form': form,
    }
  #Respond with new movie template and form
    return render(request, 'movies/movies-new.html', context)
  
  else:
    # Use MovieForm to get data from request
    # MovieForm will also make sure the data matches Movie Model
    form = MovieForm(request.POST, request.FILES)
    photo_form = PhotoForm()
    print(photo_form)
    if form.is_valid():
      movie = form.save(commit=False)
      movie.user = request.user
      movie.save()

      #Redirect to Movie detail template
      return redirect('detail', movie.id)


#=============================================================
#==DELETE==
def delete_movie(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  movie.delete()
  return redirect('index')
#=============================================================
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

#=============================================================
# ADD PHOTO WTH S3 **TO BE ADDED LATER ON**
# def add_photo(request, movie_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             s3.upload_fileobj(photo_file, BUCKET, key)
#             # build the full url string
#             url = f"{S3_BASE_URL}{BUCKET}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             photo = Photo(url=url, movie_id=movie_id)
#             photo.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('detail', movie_id=movie_id)