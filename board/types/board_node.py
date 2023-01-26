import graphene
from graphene_django import DjangoObjectType
from graphene import relay

from base import CountableConnectionBase
from board.models import Board


class BoardNode(DjangoObjectType):
    class Meta:
        model = Board
        interfaces = (relay.Node,)
        filter_fields = []
        #connection_class = CountableConnectionBase

    total_count = graphene.String()

    @staticmethod
    def resolve_total_count(_, __):
        return Board.objects.all().count()
