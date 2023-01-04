import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from base.countable_connection_base import CountableConnectionBase
from ..models import Question
from .reply_type import ReplyType


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        interfaces = (relay.Node, )
        filter_fields = {}
        connection_class = CountableConnectionBase

    replies = graphene.List(ReplyType)

    @staticmethod
    def resolve_replies(root, _):
        return root.replies.all()


