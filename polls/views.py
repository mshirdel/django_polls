from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # method 1:
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    # method 2
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    vote_result = 0
    for choice in question.choice_set.all():
        vote_result = vote_result + choice.votes

    return render(request, 'polls/results.html', {'vote_result': vote_result})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
