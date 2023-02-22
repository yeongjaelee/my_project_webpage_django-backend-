import graphene

from login.models import User


class SetToken(graphene.Mutation):
    class Arguments:
        identification = graphene.String()
        token = graphene.String()

    success = graphene.Boolean()
    @classmethod
    def mutate(cls, _, __, identification, token):
        user = User.objects.get(identification=identification)
        if token not in user.fcm_tokens:
            if len(user.fcm_tokens) == 5:
                user.fcm_tokens.remove(user.fcm_tokens[0])
            user.fcm_tokens.append(token)
        user.fcm_token = token
        user.save()

        return SetToken(success=True)
