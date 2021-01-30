from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list]) #Phase 2
    # return HttpResponse("I'm in Index") #Phase 1
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(output) # Phase 2
    # return HttpResponse(template.render(context, request)) #Phase3
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #Phase 3
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404("Question doesn't exists")
    # # return HttpResponse("You're looking at questions %s." % question_id) #Phase 1
    # return  render(request, 'polls/detail.html', {'question': question})
    #Phase 4
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question': question})


def results(request, question_id):
    response = "You're looking at the results of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)