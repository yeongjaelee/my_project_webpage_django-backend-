import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .models import Traffic
from .mutations import WriteQuestion, WriteReply
from .types import QuestionNode


class Query(graphene.ObjectType):
    questions = DjangoFilterConnectionField(QuestionNode)
    total_traffic = graphene.Int()

    @staticmethod
    def resolve_total_traffic(_, __):
        return Traffic.objects.all().count()

class Mutation(graphene.ObjectType):
    write_question = WriteQuestion.Field()
    write_reply = WriteReply.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)