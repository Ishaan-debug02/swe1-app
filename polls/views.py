from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
import json

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Get vote counts from cookies
    votes_cookie = request.COOKIES.get('poll_votes', '{}')
    try:
        votes = json.loads(votes_cookie)
    except:
        votes = {}
    
    # Apply vote counts to choices
    for choice in question.choice_set.all():
        choice_key = f"choice_{choice.id}"
        choice.votes = votes.get(choice_key, 0)
    
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
        # Get current votes from cookie
        votes_cookie = request.COOKIES.get('poll_votes', '{}')
        try:
            votes = json.loads(votes_cookie)
        except:
            votes = {}
        
        # Increment vote count
        choice_key = f"choice_{selected_choice.id}"
        votes[choice_key] = votes.get(choice_key, 0) + 1
        
        # Create response and set cookie
        response = HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        response.set_cookie('poll_votes', json.dumps(votes), max_age=86400)  # 24 hours
        return response