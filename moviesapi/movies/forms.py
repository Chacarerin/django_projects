
from django import forms

class MovieSearchForm(forms.Form):
    mood = forms.CharField(label="Describe tu estado de ánimo o algo que te motive", max_length=100, required=True)