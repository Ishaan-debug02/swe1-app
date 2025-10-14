from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class PollsIndexViewTests(TestCase):
    def test_index_page_loads(self):
        Question.objects.create(question_text="Q1", pub_date=timezone.now())
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
