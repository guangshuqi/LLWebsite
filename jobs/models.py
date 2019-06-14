from django.db import models

# Create your models here.
class Job(models.Model):
    jobtitle = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    company = models.CharField(max_length=100)