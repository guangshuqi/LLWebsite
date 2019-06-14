from django.shortcuts import render
from django.http import HttpResponse
from users.models import Job


# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'users/home.html', {'jobs':jobs})

def about(request):
    return HttpResponse('<h1>Job About</h1>')