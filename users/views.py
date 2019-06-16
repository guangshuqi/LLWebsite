from django.shortcuts import render, redirect
from .models import Job
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def homepage(request):
    context = {"jobs": Job.objects.all()}
    return render(request, "users/home.html", context)


def about(request):
    return render(request, "users/about.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("users-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
