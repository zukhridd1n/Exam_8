import graphene

from exam.graphql.mutations import Mutation
from exam.graphql.query import Query

schema = graphene.Schema(query=Query, mutation=Mutation)

__all__ =("schema",)