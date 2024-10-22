import graphene

from exam.graphql.mutates import create_project_mutate
from exam.graphql.types import ProjectType


class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        owner = graphene.String()
        assignees = graphene.List(graphene.String, required=True)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, description, owner, assignees):
        project = create_project_mutate(name, description, owner, assignees)
        return CreateProject(project=project)


class Mutation(graphene.ObjectType):


    create_project = CreateProject.Field()
