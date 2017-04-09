from django.test import TestCase, Client
from . import models
from django.contrib.auth import get_user_model

c = Client()

class Test_Models(TestCase):
    def test_Question(self):
        user = get_user_model().objects.create_user('test','1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')

        self.assertEqual(question.is_answered, False)

    def test_Answer(self):
        user = get_user_model().objects.create_user('test', '1234')
        question = models.Question(author=user, question_content='her er ett spørsmål', question_title='Tittelen')
        answer = models.Answer(author=user, question=question)

        self.assertEqual(answer.question.question_content, 'her er ett spørsmål')


class Test_Views(TestCase):
    def test_index_load(self):
        self.assertEqual(c.get('/').status_code, 200)

    def test_about(self):
        self.assertEqual(c.get('/music/create_album/').status_code, 200)