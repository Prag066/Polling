from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[0:2]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return render(request,'polls/index.html',context)
#     #return HttpResponse(template.render(context,request))

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]

        """Return the last five published questions (not including those set to be
    published in the future)."""
        return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

def detail(request,question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{"question":question})

def results(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    return render(request,'polls/results.html',{"question":question})


def vote(request,question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question,id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{"question":question,
                                   "error_message":"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
