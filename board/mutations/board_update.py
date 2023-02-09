import graphene

from board.models import Board


class BoardUpdate(graphene.Mutation):
    class Arguments:
        board_id = graphene.Int()
        title = graphene.String()
        content = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, board_id, title, content):
        board = Board.objects.get(pk=board_id)
        board.title = title
        board.content = content
        board.save()

        return BoardUpdate(success=True)