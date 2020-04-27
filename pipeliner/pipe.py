from functools import partial


class Pipe:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


_methods = {">>": "__rrshift__", "|": "__ror__", "^": "__rxor__"}


def pipeliner(operator):
    if operator not in {">>", "|", "^"}:
        raise TypeError(f"Operator can be either '>>', '^' or '|'")

    def decorator(func):
        method = _methods[operator]
        setattr(Pipe, method, Pipe.__call__)
        return Pipe(func)

    return decorator
