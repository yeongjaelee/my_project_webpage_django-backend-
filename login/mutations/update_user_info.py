import graphene

from login.models import User


class UpdateUserInfo(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        identification = graphene.String()
        username = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, user_id, identification, username):
        user = User.objects.get(pk=user_id)
        user.identification = identification
        user.username = username
        user.save()

        return UpdateUserInfo(success=True)
