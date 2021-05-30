from django import forms
from .models import Movie, UserFeedback 
# from .models import Photo


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie 
        fields = ('name', 'year', 'genre', 'description', 'image')


# S3 TO BE ADDED LATER
# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ('url',)


    
class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ('user_review',)