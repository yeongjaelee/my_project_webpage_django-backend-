import graphene
from graphene_django.filter import DjangoFilterConnectionField

from login.models import User
from login.types.user_type import UserType


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, identification=graphene.String())

    @staticmethod
    def resolve_user(_, __, identification):
        try:
            user = User.objects.get(identification=identification)
        except:
            user = None
        return user


schema = graphene.Schema(query=Query)