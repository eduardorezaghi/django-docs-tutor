from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    # Overrides the default generic view <app>/<model_name>_list.html
    # default generic view behaviour by specifying a template name
    template_name = "polls/index.html"

    # Overrides the default context template variable <question_list>
    # with a custom one
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """ "Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    # Default attribute specifying which model
    # the generic view will act upon
    model = Question

    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    # Default attribute specifying which model
    # the generic view will act upon
    model = Question

    # Overrides the default generic view <app>/<model_name>_detail.html
    # default generic view behaviour by specifying a template name
    template_name = "polls/results.html"


def vote(request, question_id):
    """View-function for voting in a question"""
    # Query for a question of given question_id in Question model database
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
