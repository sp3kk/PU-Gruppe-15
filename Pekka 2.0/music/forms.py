from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from .models import *


class QuestionForm(forms.Form):

    question_title = forms.CharField(help_text="")
    question_content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}), help_text="")

    class Meta:
        model = Question
        fields = ('question_title', 'question_content')


class AnswerForm(forms.Form):

    answer_text = forms.CharField(help_text="")

    class Meta:
        model = Question
        fields = 'answer_text'


class QuestionVotesForm(forms.ModelForm):
    CHOICES = (('+1', 'Upvote'), ('0', 'Remove vote'), ('-1', 'Downvote'))
#    CHOICES = ('+1', '0', '-1')
    val = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), help_text="Vote for something")

    class Meta:
        model = QuestionVotes
        exclude = ('question', 'user',)


class AnswerVotesForm(forms.ModelForm):
    CHOICES = (('+1', 'Upvote'), ('0', 'Remove vote'), ('-1', 'Downvote'))
    #    CHOICES = ('+1', '0', '-1')
    val = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), help_text="Vote for something")

    class Meta:
        model = QuestionVotes
        exclude = ('ans', 'user',)


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
