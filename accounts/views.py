from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signup(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)#log the user in after signing up
            return redirect('login/')
    else:
        form = UserCreationForm()
        return render(request,'accounts/signup.html',{'form':form})

@login_required
def profile(request):
    return render(request,'accounts/profile.html')


