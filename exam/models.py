from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    role = models.CharField(max_length=64)


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
    users = models.ManyToManyField(User)
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


class StaffLogin(models.Model):
    staff = models.ForeignKey(
        User,
        verbose_name=_("Staff"),
        on_delete=models.CASCADE,
        related_name='user_stafflogin',
        limit_choices_to={'is_staff': True},
    )

    session_key = models.CharField(
        max_length=40,
        verbose_name=_("Session Key"),
    )


