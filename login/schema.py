import datetime

import graphene
import graphql_jwt
import jwt
from graphene_django.filter import DjangoFilterConnectionField
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from login.models import User
from login.mutations.delete_user import DeleteUser
from login.mutations.update_password import UpdatePassword
from login.mutations.update_user_info import UpdateUserInfo
from login.mutations.user_register import UserRegister
from login.types.user_type import UserType


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, identification=graphene.String())

    @staticmethod
    def resolve_user(_, __, identification):
        user = User.objects.filter(identification=identification).first()
        return user


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    user_register = UserRegister.Field()
    delete_user = DeleteUser.Field()
    update_user_info = UpdateUserInfo.Field()
    update_password = UpdatePassword.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)