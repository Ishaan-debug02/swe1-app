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
    
    # Create choices with hardcoded vote counts
    choices_with_votes = []
    choices = list(question.choice_set.all())
    
    # Predefined vote counts for each question
    vote_data = {
        1: [25, 18, 12, 8],   # Programming language question
        2: [20, 15, 10, 7],   # Web framework question  
        3: [22, 16, 14, 6]    # Operating system question
    }
    
    default_votes = [15, 12, 8, 5]
    votes = vote_data.get(question_id, default_votes)
    
    for i, choice in enumerate(choices):
        choice_data = {
            'choice_text': choice.choice_text,
            'votes': votes[i] if i < len(votes) else 3
        }
        choices_with_votes.append(choice_data)
    
    context = {
        'question': question,
        'choices_with_votes': choices_with_votes
    }
    return render(request, 'polls/results.html', context)

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