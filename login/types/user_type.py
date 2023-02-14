from graphene_django import DjangoObjectType
import graphene
from login.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User

    success = graphene.Boolean()