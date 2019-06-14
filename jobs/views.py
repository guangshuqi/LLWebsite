from django.shortcuts import render
from django.http import HttpResponse
from jobs.models import Job


# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def about(request):
    return HttpResponse('<h1>Job About</h1>')