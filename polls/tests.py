from django.test import TestCase
from django.urls import reverse
from .models import Question, Choice
from django.utils import timezone


class QuestionModelTests(TestCase):
    def test_question_creation(self):
        """Test that a question can be created"""
        q = Question.objects.create(
            question_text="Test question?",
            pub_date=timezone.now()
        )
        self.assertEqual(q.question_text, "Test question?")

    def test_choice_creation(self):
        """Test that a choice can be created"""
        q = Question.objects.create(
            question_text="Test?",
            pub_date=timezone.now()
        )
        c = Choice.objects.create(
            question=q,
            choice_text="Test choice",
            votes=0
        )
        self.assertEqual(c.choice_text, "Test choice")


class QuestionViewTests(TestCase):
    def test_index_view(self):
        """Test that the index view returns a 200 status"""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        """Test that the detail view works"""
        q = Question.objects.create(
            question_text="Test?",
            pub_date=timezone.now()
        )
        response = self.client.get(reverse('polls:detail', args=[q.id]))
        self.assertEqual(response.status_code, 200)
