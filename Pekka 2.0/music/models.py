from django.contrib.auth.models import Permission, User
from django.db import models
import datetime
from django.template.defaultfilters import slugify

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

    def get_score(self):
        up = QuestionVotes.objects.filter(question=self, val=+1)
        down = QuestionVotes.objects.filter(question=self, val=-1)
        res = up.count()-down.count()
        return res

    def __str__(self):
        return self.question_title + " - " + self.question_content

    def vote(self, author, val):
        QuestionVotes.qvote(question=self, user=author, val=val)

    def getAuthorRating(self):
        user_questions = Question.objects.filter(author=self.author)
        user_answers = Answer.objects.filter(author=self.author)
        question_ratings = 0
        answer_ratings = 0
        for q in user_questions:
            question_ratings += q.get_score()
        for ans in user_answers:
            answer_ratings += ans.get_score()
#        return 10
        return question_ratings + answer_ratings

class Answer(models.Model):
    author = models.ForeignKey(User, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=2000)
    answer_time = models.DateTimeField()
    is_good_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

    def accept_answer(self, user):
        if self.author == user:
            self.is_good_answer = True

    def get_score(self):
        up = AnswerVotes.objects.filter(ans=self, val=+1)
        down = AnswerVotes.objects.filter(ans=self, val=-1)
        res = up.count()-down.count()
        return res

    def vote(self, author, val):
        AnswerVotes.ansvote(question=self, user=author, val=val)

    def getAuthorRating(self):
        user_questions = Question.objects.filter(author=self.author)
        user_answers = Answer.objects.filter(author=self.author)
        question_ratings = 0
        answer_ratings = 0
        for q in user_questions:
            question_ratings += q.get_score()
        for ans in user_answers:
            answer_ratings += ans.get_score()
#        return 10
        return question_ratings + answer_ratings


class QuestionVotes(models.Model):
    question = models.ForeignKey(Question)
    val = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return 'user ' + str(self.user) + ' gave ' + str(self.val) \
               + ' points to question: \' ' + str(self.question.question_title) + '\''

    @staticmethod
    def qvote(question, user, val):
        q_vote = QuestionVotes(question=question, user=user, val=val)
        existing_vote = QuestionVotes.objects.get(user=user, question=question)
        if existing_vote is None:
            q_vote.save()
        else:
            QuestionVotes.delete(user=user, question=question)
            if existing_vote[0].val != 0:
                q_vote.save()


class AnswerVotes(models.Model):
    ans = models.ForeignKey(Answer)
    val = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __str__(self):
        return 'user ' + str(self.user) + ' gave ' + str(self.val) \
               + ' points to ans: \' ' + str(self.question.question_title) + '\''

    @staticmethod
    def ansvote(answer, user, val):
        ans_vote = Answer(ans=answer, user=user, val=val)
        existing_vote = AnswerVotes.objects.get(user=user, ans=answer)
        if existing_vote is None:
            ans_vote.save()
        else:
            AnswerVotes.delete(user=user, ans=answer)
            if existing_vote[0].val != 0:
                ans_vote.save()

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
#    def vote_question(user, comment):
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
