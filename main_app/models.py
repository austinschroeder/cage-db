from django.db import models

# Create your models here.
class Movie (models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField(max_length=4)
    genre = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

#We can use the Movie class to create a Form for
#^^^^CharField - <input type="text"/>^^^^

#^^^^TextField - <textarea></textarea>^^^^
