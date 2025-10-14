from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Base vote counts
    base_votes = {1: 5, 2: 3, 3: 8, 4: 2}  # Default for each choice ID

    # Check if someone just voted
    voted_choice = request.GET.get("voted")

    # Create choices with vote counts
    choices_with_votes = []
    for choice in question.choice_set.all():
        vote_count = base_votes.get(choice.id, 1)

        # If this choice was just voted for, add 1
        if voted_choice and int(voted_choice) == choice.id:
            vote_count += 1

        choices_with_votes.append(
            {"choice_text": choice.choice_text, "votes": vote_count, "id": choice.id}
        )

    return render(
        request,
        "polls/results.html",
        {"question": question, "choices_with_votes": choices_with_votes},
    )


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
            + f"?voted={selected_choice.id}"
        )
