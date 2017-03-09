from django.contrib.auth.models import Permission, User
from django.db import models
import datetime

#hver gang man endrer her HUSK!!!!
#husk: python manage.py makemigrations
#python manage.py migrate

class Question(models.Model):

    author = models.ForeignKey(User, default=1)
    question_title = models.CharField(max_length=100)
    question_content = models.CharField(max_length=2000)
    is_answered = models.BooleanField(default=False)
    sub_code = models.CharField(max_length=10)
    ask_time = models.DateTimeField()

    def __str__(self):
        return self.question_title +" - "+ self.question_content

#    def get_votes(self):
#        return len(QuestionVotes.vote_list.filter(question=self))


class QuestionVotes(models.Model):

    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    vote_list = models.Manager

    def __init__(self, quest, voter):
        self.question = quest
        self.user = voter

    def __str__(self):
        return

    @staticmethod
    def vote(question, user):
        if QuestionVotes.vote_list.get(user=user, question=question) is None:
            q_vote = QuestionVotes(question=question, user=user)
            q_vote.save()
        else:
            QuestionVotes.vote_list.filter(user=user, question=question).delete()


# la stå inntil videre
# class CommentVotes(models.Model):

#    comment = models.ForeignKey(Comment, unique=True)
#    user = models.ForeignKey(User, unique=True)
#    vote_list = models.Manager
#
#    def __init__(self, comment, voter):
#        self.comment = comment
#        self.user = voter
#
#    @staticmethod
#    def vote(user, comment):
#        if CommentVotes.vote_list.get(user=user, comment=comment) is None:
#            c_vote = CommentVotes(comment, user)
#            c_vote.save()
#        else:
#            CommentVotes.vote_list.filter(user=user, comment=comment).delete()


#kan slettes?
class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist

#kan slettes?
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
