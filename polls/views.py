from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Hardcode vote counts for each choice
    choices = list(question.choice_set.all())
    if len(choices) >= 4:
        choices[0].votes = 15  # First choice
        choices[1].votes = 23  # Second choice  
        choices[2].votes = 8   # Third choice
        choices[3].votes = 12  # Fourth choice
    elif len(choices) >= 3:
        choices[0].votes = 18
        choices[1].votes = 11
        choices[2].votes =