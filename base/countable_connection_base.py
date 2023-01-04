from graphene import relay, Int


class CountableConnectionBase(relay.Connection):
    class Meta:
        abstract = True

    total_count = Int()
    total_unread_count = Int()

    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()

    def resolve_total_unread_count(self, info, **kwargs):
        try:
            return type(self.iterable[0]).objects.filter(date_read__isnull=True, user=info.context.user).count()
        except:
            return
