import graphene

from board.models import Board
from board.types.board_type import BoardType


class Query(graphene.ObjectType):
    board = graphene.List(BoardType)

    @staticmethod
    def resolve_board(_,__):
        return Board.objects.all()



#class Mutation(graphene.ObjectType):



schema = graphene.Schema(query=Query)