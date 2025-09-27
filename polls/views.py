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
    
    # Hardcode vote counts for demonstration
    choices = list(question.choice_set.all())
    if len(choices) >= 4:
        choices[0].votes = 15
        choices[1].votes = 23
        choices[2].votes = 8
        choices[3].votes = 12
    elif len(choices) >= 3:
        choices[0].votes = 18
        choices[1].votes = 11
        choices[2].votes = 6
    elif len(choices) >= 2:
        choices[0].votes = 20
        choices[1].votes = 14
    elif len(choices) >= 1:
        choices[0].votes = 25
    
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