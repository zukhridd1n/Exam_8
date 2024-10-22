from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        MAINTAINER = 'maintainer', 'Maintainer'
        DEVELOPER = 'developer', 'Developer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.DEVELOPER)


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    owner = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    assignees = models.TextField(blank=True)

class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    deadline = models.DateTimeField()
    owner = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    assignees = models.TextField(blank=True)

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class AccountLogin(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, verbose_name="Session Key")





