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
        image = Upload()
        file = Upload()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, info, **kwargs):
        identification = kwargs.get('identification')
        title = kwargs.get('title')
        content = kwargs.get('content')
        is_hided = kwargs.get('is_hided')
        image = kwargs.get('image')
        file = kwargs.get('file')
        user = User.objects.get(identification=identification)
        board = Board.objects.create(user=user,
                                     title=title,
                                     content=content,
                                     is_hided=is_hided,
                                     image=image)
        if image:
            board.image = image
            board.save()
        if file:
            board.file = file
            board.save()

        return BoardCreate(success=True)