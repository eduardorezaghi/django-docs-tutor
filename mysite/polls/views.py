from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

# Create your views here.
def index(request):
    """View-function for index page"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """View-function for details about a question"""
    return HttpResponse(f"You're lookin at question {question_id}.")

def results(request, question_id):
    """View-function for results about a question poll"""
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html')

def vote(request, question_id):
    """View-function for voting in a question"""
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
