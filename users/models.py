from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="images/")
    summary = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    company = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobtitle
