from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from polls.models import Question, Choice
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superuser created: username=admin, password=admin123')
        else:
            self.stdout.write('Superuser already exists')
            
        # Create sample poll questions if none exist
        if Question.objects.count() == 0:
            # Create first question
            q1 = Question.objects.create(
                question_text="What's your favorite programming language?",
                pub_date=timezone.now()
            )
            Choice.objects.create(question=q1, choice_text="Python", votes=0)
            Choice.objects.create(question=q1, choice_text="JavaScript", votes=0)
            Choice.objects.create(question=q1, choice_text="Java", votes=0)
            Choice.objects.create(question=q1, choice_text="C++", votes=0)
            
            # Create second question
            q2 = Question.objects.create(
                question_text="Which is the best web framework?",
                pub_date=timezone.now()
            )
            Choice.objects.create(question=q2, choice_text="Django", votes=0)
            Choice.objects.create(question=q2, choice_text="React", votes=0)
            Choice.objects.create(question=q2, choice_text="Vue.js", votes=0)
            Choice.objects.create(question=q2, choice_text="Angular", votes=0)
            
            self.stdout.write('Sample poll questions created')
        else:
            self.stdout.write('Poll questions already exist')