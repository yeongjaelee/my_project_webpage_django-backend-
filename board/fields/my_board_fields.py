from graphene_django.filter import DjangoFilterConnectionField


class MyBoardField(DjangoFilterConnectionField):

    @classmethod
    def resolve_queryset(
            cls, connection, iterable, info, args, filtering_args, filterset_class
    ):
        qs = super(DjangoFilterConnectionField, cls).resolve_queryset(
            connection, iterable, info, args
        )
        filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
        qs = filterset_class(data=filter_kwargs, queryset=qs, request=info.context).qs
        board_list = []
        for q in qs:
            if q.user.identification == args['identification']:
                board_list.append(q)
        return board_list
