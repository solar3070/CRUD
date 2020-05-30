from django import forms
from .models import Album

class AlbumPost(forms.ModelForm):
    class Meta:
        model = Album
        fields =  ['image', 'title', 'description']