from difflib import SequenceMatcher
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, Http404, request
from django.shortcuts import render
from django.template import Library

from pekka.models import Question

register = Library()

def similar_to():
    sub_code = 'TTM4100'
    all_questions_with_sub_code = Question.objects.filter(sub_code=sub_code)

    for questions in all_questions_with_sub_code:
        a = questions.question_content

    for questions in all_questions_with_sub_code:
        b = questions.question_content

        likhet = SequenceMatcher(None, a, b).ratio()
        if likhet >= 0.5:
            print("1")
            return b
        else:
            print("2")
            return b

register.filter(similar_to)
