import graphene
from graphene_django import DjangoObjectType
from graphene import relay

from base.count_relay_base import CountRelayBase
from board.models import Board


class BoardNode(DjangoObjectType):
    class Meta:
        model = Board
        interfaces = (relay.Node,)
        filter_fields = []
        connection_class = CountRelayBase

    board_id = graphene.Int()
    @staticmethod
    def resolve_board_id(root,_):
        return root.id
