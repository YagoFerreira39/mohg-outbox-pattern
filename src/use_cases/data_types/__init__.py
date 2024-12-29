def base_model_omit_none(meta):
    class DecoratedMeta(meta):
        def __init__(self, *args, **kwargs):
            kwargs = {key: value for key, value in kwargs.items() if value is not None}
            super().__init__(*args, **kwargs)

    return type(meta.__name__, (DecoratedMeta,), {})
