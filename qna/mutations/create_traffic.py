import graphene

from qna.models import Traffic


class CreateTraffic(graphene.Mutation):
    class Arguments:
        ip = graphene.String()

    success = graphene.Boolean(default_value=False)

    @classmethod
    def mutate(cls, _, __, ip):
        Traffic.objects.create(ip=ip)
        return CreateTraffic(success=True)

