import graphene

from board.models import Board


class BoardDelete(graphene.Mutation):
    class Arguments:
        board_id = graphene.Int()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, board_id):
        board = Board.objects.get(pk=board_id)
        board.delete()
        return BoardDelete(success=True)