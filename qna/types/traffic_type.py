from graphene_django import DjangoObjectType

from ..models import Traffic


class TrafficType(DjangoObjectType):

    class Meta:
        model = Traffic