from django import forms
from django.contrib.auth.models import User

from .models import Album, Song

class QuestionForm(forms.Form):
    question_title = forms.CharField(required = True)

    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )





class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
