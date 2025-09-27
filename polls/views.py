from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
import random

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Generate realistic vote counts for demo
    base_votes = {
        1: [15, 23, 8, 12],  # Python, JavaScript, Java, C++
        2: [18, 9, 14, 7],   # Django, React, Vue.js, Angular  
        3: [22, 11, 16, 5]   # Windows, macOS, Linux, Other
    }
    
    vote_counts = base_votes.get(question_id, [5, 8, 12, 3])
    
    for i, choice in enumerate(question.choice_set.all()):
        if i < len(vote_counts):
            choice.votes = vote_counts[i]
        else:
            choice.votes = random.randint(1, 10)
    
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))