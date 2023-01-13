from graphene_django import DjangoObjectType

from login.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User