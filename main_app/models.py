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



#We can use the Movie class to create a Form for
#^^^^CharField - <input type="text"/>^^^^

#^^^^TextField - <textarea></textarea>^^^^
