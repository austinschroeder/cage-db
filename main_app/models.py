from django.db import models
from django.contrib.auth.models import User


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
    #Foreign key will add '_id' to field name
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            this = Movie.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(Movie, self).save(*args, **kwargs)

class Review (models.Model):
    user_review = models.TextField(
        max_length=400,
        null=True,
        blank=True
    )



#We can use the Movie class to create a Form for
#^^^^CharField - <input type="text"/>^^^^

#^^^^TextField - <textarea></textarea>^^^^
