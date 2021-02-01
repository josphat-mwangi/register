from django.shortcuts import render,redirect
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    return render(request, 'index.html')



def register(response):
    if response.method == "POST":
        form = RegisterUserForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = RegisterUserForm()
    return render(response,'registration/register.html',{'form':form})