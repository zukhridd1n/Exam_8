import graphene

from exam.graphql.types import UserType, TaskType, ProjectType, CommentType, NotificationType


class Query(graphene.ObjectType):
    all_user = graphene.List(UserType)
    tasks = graphene.List(TaskType)
    projects = graphene.List(ProjectType)
    comments = graphene.List(CommentType)
    notifications = graphene.List(NotificationType)


    

