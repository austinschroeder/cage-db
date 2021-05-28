from django import forms
from .models import Movie, UserFeedback 

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie 
        fields = ('name', 'year', 'genre', 'description', 'image')
    
class UserFeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ('user_review',)