from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from PIL import Image

# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Job(models.Model):
    jobtitle = models.CharField(max_length=50, default="")
    image = models.ImageField(default="default.jpg", upload_to="Job_pics/")
    summary = models.TextField()
    startdate = models.DateField()
    enddate = models.DateField()
    company = models.CharField(max_length=100)
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobtitle
