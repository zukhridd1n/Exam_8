from graphene_django import DjangoObjectType

from exam.models import User, Project, Task, Comment, Notification


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'role')


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'owner', 'created_at', 'assignees')


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'user', 'created_at', 'assignees', 'status', 'deadline')

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'task', 'author', 'created_at')

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'message', 'created_at', 'type', 'is_read')