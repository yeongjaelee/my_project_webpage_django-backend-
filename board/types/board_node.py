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
        # connection_class = CountableConnectionBase

    total_count = graphene.String()
    board_id = graphene.Int()
    @staticmethod
    def resolve_total_count(_, __):
        return Board.objects.all().count()

    @staticmethod
    def resolve_board_id(root,_):
        return root.id
