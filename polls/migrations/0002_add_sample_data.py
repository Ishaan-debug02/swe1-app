from django.db import migrations
from django.utils import timezone

def create_sample_data(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Choice = apps.get_model('polls', 'Choice')
    
    q1 = Question.objects.create(
        question_text="What's your favorite programming language?",
        pub_date=timezone.now()
    )
    Choice.objects.create(question=q1, choice_text="Python", votes=0)
    Choice.objects.create(question=q1, choice_text="JavaScript", votes=0)
    Choice.objects.create(question=q1, choice_text="Java", votes=0)
    Choice.objects.create(question=q1, choice_text="C++", votes=0)
    
    q2 = Question.objects.create(
        question_text="Which is the best web framework?",
        pub_date=timezone.now()
    )
    Choice.objects.create(question=q2, choice_text="Django", votes=0)
    Choice.objects.create(question=q2, choice_text="React", votes=0)
    Choice.objects.create(question=q2, choice_text="Vue.js", votes=0)
    Choice.objects.create(question=q2, choice_text="Angular", votes=0)

def reverse_data(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Question.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_data, reverse_data),
    ]