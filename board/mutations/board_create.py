import graphene

from board.models import Board
from login.models import User


class BoardCreate(graphene.Mutation):
    class Arguments:
        identification = graphene.String()
        title = graphene.String()
        content = graphene.String()
        is_hided = graphene.Boolean()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, info, title, content, is_hided, identification):
        print(1)
        user = User.objects.get(identification=identification)
        Board.objects.create(user=user,
                             title=title,
                             content=content,
                             is_hided=is_hided)

        return BoardCreate(success=True)