from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,Profile,Publication,Article
from .forms import QuestionForm,UserSignupForm,Log_inForm
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:2]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request,'polls/index.html',context)
    #return HttpResponse(template.render(context,request))

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

def success(request):
    return render(request,'polls/success.html')

class QuestionFormView(CreateView):
    model = Question
    template_name = 'polls/models/question.html'
    fields = '__all__'
    success_url = '/polls/success/'

def Questionform(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionForm()
    return render(request,'polls/models/question.html',{"form":form})

# display list of questions
def qdata(request):
    listdata = Question.objects.all()
    return render(request,'polls/models/data.html',{"listdata":listdata})

# display and update data
def detailqus(request,id=None):
    details = Question.objects.get(id=id)
    if request.method=="POST":
        form = QuestionForm(request.POST,instance=details)
        if form.is_valid():
            form.save()
            return redirect('/polls/success/')
    else:
        form = QuestionForm(instance=details)
    return render(request,'polls/models/datadetals.html',{"details":details,"form":form})

# to delete a perticular data
def detaildel(request,id=None):
    details = Question.objects.get(id=id)
    details.delete()
    return render(request,'polls/models/datadetals.html',{"details":details})

def sign_upview(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            send_mail('django','django mail','cabdatabase.finalyearproject@gmail.com',[email,],fail_silently=True)
            User.objects.create_user(username=username,email=email,password=password)
    else:
        form = UserSignupForm()
    return render(request,'auth/sign_upview.html',{"form":form})

def log_inview(request):
    if request.method == "POST":
        form = Log_inForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'base.html',{"user":user})
    else:
        form = Log_inForm()
    return render(request,'auth/login.html',{"form":form})

def log_outview(request):
    logout(request)
    return redirect('/polls/log_inview/')

def profiledetail(request):
    data=Profile.objects.all()
    return render(request,'profiledata/profiledata.html',{"data":data})

def articledetail(request):
    article_data=Article.objects.all()
    return render(request,'article/article_data.html',{"article_data":article_data})

def createAP(r):
    p=Publication(title='new_pub')
    p.save()
    p1=Publication(title='new_pub1')
    p1.save()
    a=Article(headline='new_headline')
    a.save()
    a.publications.add(p,p1)
    return render(r,'ap.html',{'a':a})
