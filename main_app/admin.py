from django.contrib import admin
from .models import Movie, UserFeedback, Photo

# Register models.
admin.site.register(Movie)
admin.site.register(UserFeedback)
admin.site.register(Photo)
