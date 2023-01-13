import graphene
from graphene_django.filter import DjangoFilterConnectionField

from login.models import User
from login.types.user_type import UserType


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, identification=graphene.String())

    @staticmethod
    def resolve_user(_, __, identification):
        return User.objects.get(identification=identification)


schema = graphene.Schema(query=Query)