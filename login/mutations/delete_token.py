import graphene

from login.models import User


class DeleteToken(graphene.Mutation):
    class Arguments:
        token = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, token):
        user = User.objects.get(fcm_token=token)
        user.fcm_token=''
        user.save()

        return DeleteToken(success=True)