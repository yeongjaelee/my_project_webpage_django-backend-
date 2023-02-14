import graphene

from login.models import User


class UpdatePassword(graphene.Mutation):
    class Arguments:
        identification = graphene.String()
        password = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, identification, password):
        print(1)
        user = User.objects.get(identification=identification)
        print(user.identification)
        user.set_password(password)
        user.save()

        return UpdatePassword(success=True)