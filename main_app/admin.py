from django.contrib import admin
from .models import Movie, UserFeedback
# from .models import Photo

# Register models.
# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(UserFeedback)
# admin.site.register(Photo)


