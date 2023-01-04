import graphene

from qna.models import Reply


class WriteReply(graphene.Mutation):
    class Arguments:
        question_id = graphene.Int()
        contents = graphene.String(required=True)

    success = graphene.Boolean(default_value=False)

    @classmethod
    def mutate(cls, _, info, question_id, contents):
        user = info.context.user
        Reply.objects.create(question_id=question_id, contents=contents, user=user)
        return WriteReply(success=True)
