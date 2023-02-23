import graphene

from login.models import User


class UserRegister(graphene.Mutation):
    class Arguments:
        identification = graphene.String()
        username = graphene.String()
        password = graphene.String()
        address = graphene.String()
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, _, __, identification, username, password, address):
        User.objects.create_user(identification=identification,
                                 username=username,
                                 password=password,
                                 address=address)

        return UserRegister(success=True)