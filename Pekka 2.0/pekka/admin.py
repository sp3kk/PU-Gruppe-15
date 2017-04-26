from django.contrib import admin
from .models import *

admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_title', 'question_content']}),
        ('Date info', {'fields': ['ask_time']}),
    ]
    inlines = [AnswerInline]
    list_display = ['question_title', 'question_content', "ask_time"]

admin.site.register(Question, QuestionAdmin, )
