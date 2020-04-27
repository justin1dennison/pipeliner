from functools import partial


def call(obj, other):
    return obj(other)


class Pipe:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    __rrshift__ = __ror__ = __rxor__ = call


def pipeliner(operator):
    if operator not in {">>", "|", "^"}:
        raise TypeError(f"Operator can be either '>>', '^' or '|'")

    def decorator(func):
        return Pipe(func)

    return decorator
