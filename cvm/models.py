from django.contrib.auth.models import User
from django.db import models


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cv", null=True)
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=14, null=True)
    email = models.EmailField(null=True)
    skills = models.CharField(max_length=300)
    interests = models.CharField(max_length=300)
    about = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV for {self.name}"


class Experience(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="experience", null=True)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    work = models.CharField(max_length=400)
    duration = models.CharField(max_length=200)


class Education(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="education", null=True)
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    score = models.CharField(max_length=50)
