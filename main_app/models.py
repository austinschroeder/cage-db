from django.db import models

# Create your models here.
class Movie (models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField(
        max_length=300,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True, 
        blank=True, 
        upload_to="images/"
    )



#We can use the Movie class to create a Form for
#^^^^CharField - <input type="text"/>^^^^

#^^^^TextField - <textarea></textarea>^^^^
