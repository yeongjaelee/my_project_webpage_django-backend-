import graphene

from board.models import Board


class DeleteBoards(graphene.Mutation):
    class Arguments:
        board_ids = graphene.List(graphene.Int)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, board_ids):
        Board.objects.filter(id__in=board_ids).delete()

        return DeleteBoards(success=True)