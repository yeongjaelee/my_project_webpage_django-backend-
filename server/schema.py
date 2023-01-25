import graphene

import board.schema
import login.schema
import qna.schema

class Query(qna.schema.Query,
            login.schema.Query,
            board.schema.Query):
    pass


class Mutation(qna.schema.Mutation,
               login.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)