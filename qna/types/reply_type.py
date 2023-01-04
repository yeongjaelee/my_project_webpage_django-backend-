from graphene_django import DjangoObjectType

from ..models import Reply


class ReplyType(DjangoObjectType):

    class Meta:
        model = Reply