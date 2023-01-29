import graphene
from graphene_django import DjangoObjectType

from board.models import Board


class BoardType(DjangoObjectType):
    class Meta:
        model = Board
