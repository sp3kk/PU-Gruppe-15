from django.test import RequestFactory
from django.test import TestCase, Client

from music.forms import QuestionForm
from . import models
from . import views
from django.contrib.auth import get_user_model


c = Client()

<<<<<<< HEAD:Pekka 2.0/music/tests.py
class Test_Models(TestCase):

=======

class TestModels(TestCase):
>>>>>>> ff00d97f5be37b8890a0f2d96329151bcb19e0c9:Pekka 2.0/pekka/tests.py
    def test_Question(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')

        self.assertEqual(question.is_answered, False)

    def test_Answer(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        answer = models.Answer(author=user, question=question)

        self.assertEqual(answer.question.question_content, 'her er ett spørsmål')

    def test_QuestionVotes(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        q_vote = models.QuestionVotes(question=question, user=user, val=0)
        existing_vote = None

        """"self.assertEqual(q_vote, 0)"""""


<<<<<<< HEAD:Pekka 2.0/music/tests.py
class Test_Views(TestCase):

=======
class TestViews(TestCase):
>>>>>>> ff00d97f5be37b8890a0f2d96329151bcb19e0c9:Pekka 2.0/pekka/tests.py
    def test_index_load(self):
        self.assertEqual(c.get('/').status_code, 200)

    def test_about(self):
<<<<<<< HEAD:Pekka 2.0/music/tests.py
        self.assertEqual(c.get('/music/create_album/').status_code, 200)

    def test_TDT4110_a(self):
        self.assertEqual(c.get('/music/TDT4110_a/').status_code, 200)
    def test_TDT4110_q(self):
        self.assertEqual(c.get('/TDT4110_q/').status_code, 200)

    def test_TDT4140_a(self):
        self.assertEqual(c.get('/music/TDT4140_a/').status_code, 200)
    def test_TDT4140_q(self):
        self.assertEqual(c.get('/TDT4140_q/').status_code, 200)

    def test_TDT4145_a(self):
        self.assertEqual(c.get('/music/TDT4145_a/').status_code, 200)
    def test_TDT4145_q(self):
        self.assertEqual(c.get('/TDT4145_q/').status_code, 200)

    def test_TDT4180_a(self):
        self.assertEqual(c.get('/music/TDT4180_a/').status_code, 200)
    def test_TDT4180_q(self):
        self.assertEqual(c.get('/TDT4180_q/').status_code, 200)

    def test_TTM4100_a(self):
        self.assertEqual(c.get('/music/TTM4100_a/').status_code, 200)
    def test_TTM4100_q(self):
        self.assertEqual(c.get('/TTM4100_q/').status_code, 200)
    def test_TTM4100_b(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        question.save()
        a = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen2')
        a_content = a.question_content
        a.save()
        self.assertEqual(question.question_content, a_content)
        self.assertEqual(c.get('/TTM4100_b/').status_code, 200)




    def test_addQuestion(self):
        request = RequestFactory().post(
            '/Fagsider/questions.html/',
            {
                'title': 'Some title',
                'body': 'Some text',
            }
        )
        form = QuestionForm(request.POST)
        form.is_valid = True
        response = views.addQuestion(request)
        self.assertEqual(response.status_code, 200)
=======
        self.assertEqual(c.get('/pekka/about/').status_code, 200)
>>>>>>> ff00d97f5be37b8890a0f2d96329151bcb19e0c9:Pekka 2.0/pekka/tests.py
