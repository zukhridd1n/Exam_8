import graphene
from exam.graphql.resolvers import resolve_all_notifications, resolve_all_projects, resolve_all_tasks, resolve_all_comments, resolve_notification, resolve_project, resolve_task, resolve_comment
from exam.graphql.types import UserType, TaskType, ProjectType, CommentType, NotificationType


class Query(graphene.ObjectType):
    all_user = graphene.List(UserType)
    tasks = graphene.List(TaskType)
    projects = graphene.List(ProjectType)
    comments = graphene.List(CommentType)
    notifications = graphene.List(NotificationType)

    def resolve_notifications(self, info, **kwargs):
        return resolve_all_notifications()

    def resolve_projects(self, info, **kwargs):
        return resolve_all_projects()

    def resolve_tasks(self, info, **kwargs):
        return resolve_all_tasks()

    def resolve_comments(self, info, **kwargs):
        return resolve_all_comments()

    def resolve_notification(self, info, id, **kwargs):
        return resolve_notification(id=id)

    def resolve_project(self, info, id, **kwargs):
        return resolve_project(id=id)

    def resolve_task(self, info, id, **kwargs):
        return resolve_task(id=id)

    def resolve_comment(self, info, id, **kwargs):
        return resolve_comment(id=id)


