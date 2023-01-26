import graphene
from graphene_django.filter import DjangoFilterConnectionField

from board.models import Board
from board.types.board_node import BoardNode


class Query(graphene.ObjectType):
    board = DjangoFilterConnectionField(BoardNode)

    @staticmethod
    def resolve_board(_,__):
        return Board.objects.all()



#class Mutation(graphene.ObjectType):



schema = graphene.Schema(query=Query)