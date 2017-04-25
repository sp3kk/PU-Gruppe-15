from difflib import SequenceMatcher

from django.http import Http404
from django.test import RequestFactory
from django.test import TestCase, Client
from unittest.mock import patch, MagicMock
from django.core.urlresolvers import reverse
from pekka.forms import QuestionForm
from . import models
from . import views
from . import forms
from django.contrib.auth import get_user_model

c = Client()


class TestModels(TestCase):
    def test_Question(self):

        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')

        self.assertEqual(question.is_answered, False)

        self.assertEqual(question.ask_time, '2017-4-17T09:21:31+0000')


    def test_Answer(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        answer = models.Answer(author=user, question=question)

        self.assertEqual(answer.question.question_content, 'her er ett spørsmål')
        self.assertEqual(question.author, user)

    def test_QuestionVotes(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question_vote = models.QuestionVotes(question=question, user=user, question_id=1)
        question.save()
        question_vote.save()

        self.assertEqual(question_vote.val, 0)

        q_vote = models.QuestionVotes(question=question, user=user, val=0)
        existing_vote = models.QuestionVotes.objects.get(user=user, question=question, question_id=1)

        self.assertIsNotNone(existing_vote)
        self.assertTrue(q_vote, True)


class Test_Views(TestCase):
    def test_index_load(self):
        self.assertEqual(c.get('/').status_code, 200)

    def test_about(self):
        self.assertEqual(c.get('/pekka/about/').status_code, 200)

    def test_ask(self):
        self.assertEqual(c.get('/').status_code, 200)
        user = get_user_model().objects.create_user('test', '1234')
        c.login(username='test', password='1234')
        self.assertEqual(c.get('/pekka/login_user/').status_code, 200)

    def test_logout_user(self):
        c.login(username='test', password='1234')
        c.logout()
        self.assertEqual(c.get('/pekka/logout_user/').status_code, 200)

    def test_login_user(self):
        c.login(username='test', password='1234')
        self.assertEqual(c.get('/pekka/login_user/').status_code, 200)
        c.logout()
        self.assertEqual(c.get('/pekka/logout_user/').status_code, 200)

        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()

        self.assertTrue(user.is_active)

        self.assertEqual(c.get('/pekka/ask/').status_code, 200)
        self.assertEqual(c.get('/ask/').status_code, 200)
        self.assertEqual(c.get('/pekka/answer/').status_code, 200)
        self.assertEqual(c.get('/answer/').status_code, 200)

    def test_register(self):
        c.login(username='test', password='1234')
        self.assertEqual(c.get('/pekka/login_user/').status_code, 200)
        c.logout()
        self.assertEqual(c.get('/pekka/logout_user/').status_code, 200)
        self.assertEqual(c.get('/pekka/register/').status_code, 200)

    def test_detail(self):

        self.assertRaises(Http404)
        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        try:
            question_get = views.Question.objects.get(pk=question.id)
            self.assertTrue(question_get, True)

        except views.Question.DoesNotExist:
            self.assertEqual(c.get('/1/').status_code, 200)

    def test_TDT4110_a(self):
        self.assertEqual(c.get('/pekka/TDT4110_a/').status_code, 200)

    def test_TDT4110_q(self):
        self.assertEqual(c.get('/TDT4110_q/').status_code, 200)

        form = QuestionForm()
        form.is_valid()
        self.assertEqual(c.get('/TDT4110_b/').status_code, 200)

    def test_TDT4140_a(self):
        self.assertEqual(c.get('/pekka/TDT4140_a/').status_code, 200)

    def test_TDT4140_q(self):
        self.assertEqual(c.get('/TDT4140_q/').status_code, 200)

        form = QuestionForm()
        form.is_valid()
        self.assertEqual(c.get('/TDT4140_b/').status_code, 200)

    def test_TDT4145_a(self):
        self.assertEqual(c.get('/pekka/TDT4145_a/').status_code, 200)

    def test_TDT4145_q(self):
        self.assertEqual(c.get('/TDT4145_q/').status_code, 200)

        form = QuestionForm()
        form.is_valid()
        self.assertEqual(c.get('/TDT4145_b/').status_code, 200)

    def test_TDT4180_a(self):
        self.assertEqual(c.get('/pekka/TDT4180_a/').status_code, 200)

    def test_TDT4180_q(self):
        self.assertEqual(c.get('/TDT4180_q/').status_code, 200)

        form = QuestionForm()
        form.is_valid()
        self.assertEqual(c.get('/TDT4180_b/').status_code, 200)

    def test_TTM4100_a(self):
        self.assertEqual(c.get('/pekka/TTM4100_a/').status_code, 200)

    def test_TTM4100_q(self):
        self.assertEqual(c.get('/TTM4100_q/').status_code, 200)

        form = QuestionForm()
        form.is_valid()
        self.assertEqual(c.get('/TTM4100_b/').status_code, 200)

    def test_TDT4110_b(self):
        self.assertEqual(c.get('/TDT4110_b/').status_code, 200)

    def test_TDT4140_b(self):
        self.assertEqual(c.get('/TDT4140_b/').status_code, 200)

    def test_TDT4145_b(self):
        self.assertEqual(c.get('/TDT4145_b/').status_code, 200)

    def test_TDT4180_b(self):
        self.assertEqual(c.get('/TDT4180_b/').status_code, 200)

    def test_TTM4100_b(self):
        self.assertEqual(c.get('/TTM4100_b/').status_code, 200)


    def test_vote_question(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        question_form = QuestionForm()
        self.assertEqual(question_form.is_valid(), False)  # No data has been supplied yet.
        question_form = QuestionForm({'question_content': "her er ett spørsmål", 'question_title': 'Tittelen', })
        self.assertEqual(question_form.is_valid(), True)  # Now that you have given it data, it can validate.
        self.assertEqual(c.get('/1/').status_code, 200)

        client = Client()
        response = client.post('/pekka/1/vote_question/')
        form = QuestionForm()
        self.assertEqual(form.is_valid(), False)  # No data has been supplied yet.
        form = QuestionForm({'question_content': "her er ett spørsmål", 'question_title': 'Tittelen', })
        self.assertEqual(form.is_valid(), True)  # Now that you have given it data, it can validate.
        views.request.method = 'POST'
        #self.assertRedirects(response, '/1/')
        self.assertEqual(c.get('/1/').status_code, 200)
        self.assertEqual(c.get('/pekka/1/').status_code, 200)

    def test_vote_answer(self):

        import datetime
        now = datetime.datetime.now()

        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        answer = views.Answer(answer_text='Svaret er 42', answer_time=now, question_id=1)
        answer.save()
        question_form = QuestionForm()
        self.assertEqual(question_form.is_valid(), False)  # No data has been supplied yet.
        question_form = QuestionForm({'question_content': "her er ett spørsmål", 'question_title': 'Tittelen', })
        self.assertEqual(question_form.is_valid(), True)  # Now that you have given it data, it can validate.
        self.assertEqual(c.get('/pekka/1/vote_answer/').status_code, 200)
        self.assertEqual(c.get('/1/vote_answer/').status_code, 200)

    def test_answer(self):
        self.assertEqual(c.get('/answer/').status_code, 200)
        self.assertEqual(c.get('/pekka/answer/').status_code, 200)

    def test_detail(self):
        import datetime
        now = datetime.datetime.now()
        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        answer = views.Answer(answer_text='Svaret er 42', answer_time=now, question_id=1)
        answer.save()
        self.assertEqual(c.get('/pekka/1/').status_code, 200)

    def test_course_b(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen',
                                  sub_code='TTM4100')
        question.save()
        all_questions_with_sub_code = views.Question.objects.filter(sub_code='TTM4100').latest('ask_time')
        a_content = all_questions_with_sub_code.question_content
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        b = question.question_content
        likhet = SequenceMatcher(None, a_content, b).ratio()
        self.assertGreaterEqual(likhet, 0.5)
        self.assertIsNotNone(all_questions_with_sub_code)
        self.assertEqual(c.get('/TTM4100_b/').status_code, 200)

    def test_course_q(self):

        import datetime
        now = datetime.datetime.now()

        user = get_user_model().objects.create_user('test', '1234')
        question = views.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        answer = views.Answer(answer_text='Svaret er 42', answer_time=now, question_id=1)
        answer.save()
        form = QuestionForm()
        self.assertEqual(form.is_valid(), False)  # No data has been supplied yet.
        form = QuestionForm({'question_content': "her er ett spørsmål", 'question_title': 'Tittelen', })
        self.assertEqual(form.is_valid(), True)  # Now that you have given it data, it can validate.
        self.assertEqual(c.get('/pekka/TDT4140_q/').status_code, 200)
        views.request.method = 'POST'



    def test_call_view_loads(self):
        user = get_user_model().objects.create_user('test', '1234')
        self.client.login(user=user)  # defined in fixture or with factory in setUp()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'html_pages/login.html', 'html_pages/base_visitor.html')
