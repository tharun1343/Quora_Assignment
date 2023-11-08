from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

#function for home page
def home(request):
      ques = Question.objects.prefetch_related("answers_set").all()
      return render(request,'home.html', context={'ques' : ques})

# function for registration.
def register(request):
    if request.method == 'POST':
        data1 = RegisterForm(request.POST)
        if data1.is_valid():
            data1.save()
            return redirect('login')
        messages.error(request,"Please enter the details correctly")
    data1 = RegisterForm()
    return render(request,'register.html',context={'form' : data1})

# function for user login.
def user_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,'login.html', context={"login_form":form})

# function for user logout.
def loggout(request):
	logout(request)
	return redirect('login')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = Add_Question(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user_id_id = request.user.id
            question.save()
            return redirect('home')
    else:
        form = Add_Question()
    return render(request, 'post_question.html', {'form': form})

@login_required
def ans_question(request, id):
    question = Question.objects.get(id = id)
    if request.method == 'POST':
        form = Add_answer(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user_id_id = request.user.id
            answer.question_id_id = question.id
            answer.save()
            return redirect('home')
    else:
        form = Add_answer()
    return render(request, 'ans_question.html', {'form': form})

def addlike(request):
      ans = get_object_or_404(Answers, id = request.POST.get('answer_id'))
      ans.likes.add(request.user)
      return HttpResponseRedirect(reverse('home'))