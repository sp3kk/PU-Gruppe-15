from django.contrib.auth.models import Permission, User
from django.db import models
from _datetime import timezone

class Question(models.Model):
    author=models.ForeignKey(User, default=1)
    ask_time= timezone
    question_title=models.CharField(max_length=100)
    question_content=models.CharField(max_length=2000)
    is_answered=models.BooleanField(default=False)
    sub_code=models.CharField(max_length=10)
    def __str__(self):
        return (self,self.author,self.ask_time, self.question_title, self.question_content)




class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
