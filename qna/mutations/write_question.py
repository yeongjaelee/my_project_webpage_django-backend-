import graphene

from qna.models import Question


class WriteQuestion(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        contents = graphene.String(required=True)

    success = graphene.Boolean(default_value=False)

    @classmethod
    def mutate(cls, _, __, email, contents):
        Question.objects.create(email=email, contents=contents)
        return WriteQuestion(success=True)

