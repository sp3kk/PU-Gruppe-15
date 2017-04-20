from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from .models import *


class QuestionForm(forms.Form):

    question_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="")
    question_content = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,
                                                                    'rows': 10,
                                                                    'class': 'form-control'}), help_text="")

    class Meta:
        model = Question
        fields = ('question_title', 'question_content')


class AnswerForm(forms.Form):

    answer_text = forms.CharField(widget=forms.Textarea(attrs={'cols': 30,
                                                               'rows': 10,
                                                               'class': 'form-control'}), help_text="")

    class Meta:
        model = Answer
        fields = 'answer_text'


class QuestionVotesForm(forms.ModelForm):
    UP = '+1'
    REMOVE = '0'
    DOWN = '-1'
    CHOICES = ((UP, 'Upvote'), (REMOVE, 'Remove vote'), (DOWN, 'Downvote'))
#    CHOICES = ('+1', '0', '-1')
    val = forms.ChoiceField(label="", choices=CHOICES, widget=forms.RadioSelect(), help_text="Don't forget to submit!")

    class Meta:
        model = QuestionVotes
        exclude = ('question', 'user', 'val')


class AnswerVotesForm(forms.ModelForm):
    CHOICES = (('+1', 'Upvote'), ('0', 'Remove vote'), ('-1', 'Downvote'))
    #    CHOICES = ('+1', '0', '-1')
    val = forms.ChoiceField(label="", choices=CHOICES, widget=forms.RadioSelect(), help_text="Don't forget to submit!")

    class Meta:
        model = AnswerVotes
        exclude = ('ans', 'user', 'val')


class UserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), help_text="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SignInForm(forms.ModelForm):

    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="")

    class Meta:
        model = User
        fields = ['username', 'password']
