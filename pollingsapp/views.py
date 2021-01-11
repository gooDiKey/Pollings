from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, response
from .models import Polling, Question, Option, Answer
from django.urls import reverse
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def home(request):
    return render(request, 'pollingsapp/home.html')

def index(request):
    pollings = Polling.objects
    return render(request, 'pollingsapp/index.html', {'pollings': pollings})

def poll(request, polling_id):
    print(request.POST)
    polling = get_object_or_404(Polling, pk=polling_id)
    return render(request, 'pollingsapp/poll.html', {'polling': polling})

def question(request, polling_id, question_id):
    polling = get_object_or_404(Polling, pk=polling_id)
    questions = get_object_or_404(Question, pk=question_id)
    return render(request, 'pollingsapp/poll.html', {'polling': polling, 'questions': questions})

def result(request, polling_id):
    polling = get_object_or_404(Polling, pk=polling_id)
    results = {}
    for question in polling.question_set.all():
        results[question.question_text] = (question.answer_set.filter(user = request.user.id, question = question.id))
    user = request.user.id

    return render(request, 'pollingsapp/results.html', {'polling': polling, 'results': results, 'use': user})

def vote(request, polling_id):
    polling = get_object_or_404(Polling, pk=polling_id)
    answers = {}
    for question in polling.question_set.all():
        try:
            if isinstance(request.POST[str(question.id)], int):
                selected_option = question.option_set.get(pk=request.POST[str(question.id)])
            else:
                selected_option = request.POST[str(question.id)]
        except (KeyError, Option.DoesNotExist):
            return render(request, 'pollingsapp/poll.html', {'polling': polling, 'error_message': "Вы не ответили на один или несколько вопросов"})
        else:
            answers[question.id] = selected_option
    # line = []
    # for question in answers:
    #     line.append(question)
    #     line.append(answers[question])
    # return render(request, 'pollingsapp/vote.html', {'answers': answers, 'line': line})
    for question in answers:
        answer = Answer()
        answer.question_id = question
        answer.user_id = request.user.id
        answer.answer_text = answers[question]
        answer.save()
    return HttpResponseRedirect(reverse('pollingsapp:results', args=(polling_id,)))




def signUpView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            user_group = Group.objects.get(name='User')
            user_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'pollingsapp/signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('pollingsapp:signup')
    else:
        form = AuthenticationForm()
    return render(request, 'pollingsapp/login.html', {'form': form})

def signoutView(request):
    logout(request)
    return redirect('pollingsapp:login')