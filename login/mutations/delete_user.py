import graphene

from login.models import User


class DeleteUser(graphene.Mutation):
    class Arguments:
        identification = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, identification):
        user = User.objects.get(identification=identification)
        user.delete()
        return DeleteUser(success=True)
