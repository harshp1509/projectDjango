from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate ,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.froms import SuggestionForm
from app.models import Suggestion
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=SuggestionForm()
        ss=Suggestion.objects.filter(user=user)
        return render(request,'index.html',context={'form':form,'ss':ss})

def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        context={
           'form':form
        }
        return render(request,'login.html',context=context)

    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')

        else:
             context={
           'form':form
        }
        return render(request,'login.html',context=context)


def signup(request):
    if request.method=='GET':
        form=UserCreationForm()
        contect={
            "form":form
        }
        return render(request,'signup.html',context=contect)
    else:
        form=UserCreationForm(request.POST)
        contect={
            "form":form
        }
        if form.is_valid():
            user=form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request,'signup.html',context=contect)

@login_required(login_url='login')
def add_suggestion(request):
    if request.user.is_authenticated:
        user=request.user
        form=SuggestionForm(request.POST)
        if form.is_valid():
            ss=form.save(commit=False)
            ss.user=user
            ss.save()
            return redirect('home')
        else:
            return render(request,"index.html",context={'form':form})

def signout(request):
    logout(request)
    return redirect(login)

def delete_sug(request,id):
    Suggestion.objects.get(pk=id).delete()
    return redirect('home')
