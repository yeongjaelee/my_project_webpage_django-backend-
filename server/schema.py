import graphene
import qna.schema

class Query(qna.schema.Query):
    pass


class Mutation(qna.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)