from graphene import Connection, Int


class CountRelayBase(Connection):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length

