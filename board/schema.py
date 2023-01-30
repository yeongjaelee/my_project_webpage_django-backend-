import graphene
from graphene_django.filter import DjangoFilterConnectionField

from board.models import Board
from board.mutations.board_create import BoardCreate
from board.types.board_node import BoardNode
from board.types.board_type import BoardType
from login.models import User


class Query(graphene.ObjectType):
    board = DjangoFilterConnectionField(BoardNode)
    my_board = DjangoFilterConnectionField(BoardNode, identification=graphene.String())
    board_detail = graphene.Field(BoardType, board_id=graphene.Int())
    """
    @staticmethod
    def resolve_board(_,__):
        return Board.objects.all()
        """
    # @staticmethod
    # def resolve_my_board(_, __, identification, ):
    #     user = User.objects.get(identification=identification)
    #     return Board.objects.filter(user=user)
    @staticmethod
    def resolve_board_detail(_, __, board_id):
        return Board.objects.get(id=board_id)
class Mutation(graphene.ObjectType):
    board_create = BoardCreate.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)