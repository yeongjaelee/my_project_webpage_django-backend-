import graphene
from graphene_file_upload.scalars import Upload

from board.models import Board
from login.models import User


class BoardCreate(graphene.Mutation):
    class Arguments:
        identification = graphene.String()
        title = graphene.String()
        content = graphene.String()
        is_hided = graphene.Boolean()
        file = Upload()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, info, title, content, is_hided, identification, file):
        print(1)
        user = User.objects.get(identification=identification)
        print(title)
        print(file)
        Board.objects.create(user=user,
                             title=title,
                             content=content,
                             is_hided=is_hided,
                             file=file)

        return BoardCreate(success=True)