import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms

class CV(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="cv",null=True)
    name = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=14,null=True)
    email = models.EmailField(null=True)
    skills = models.CharField(max_length=300)
    interests = models.CharField(max_length=300)
    about = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)


class Experience(models.Model) :
    cv = models.ForeignKey(CV,on_delete=models.CASCADE,related_name="experience",null=True)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    work  = models.CharField(max_length=400)
    duration = models.CharField(max_length=200)

class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE,related_name="education", null=True)
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    score = models.CharField(max_length=50)








