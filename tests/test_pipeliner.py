from pipeliner import __version__, pipeliner


def _square(x: int) -> int:
    return x * x


def _inc(x: int) -> int:
    return x + 1


def test_version():
    assert __version__ == "0.1.0"


def test_pipeliner():
    square = pipeliner(">>")(_square)
    inc = pipeliner(">>")(_inc)
    result = square(2) >> inc >> square

    assert result == 25


def test_pipeliner_with_other_operators():
    square = pipeliner("|")(_square)
    inc = pipeliner("|")(_inc)
    result = square(2) | inc | square

    assert result == 25

def test_pipeliner_with_strings():
    @pipeliner(">>")
    def double(xs: list):
        return (2 * x for x in xs)

    @pipeliner(">>")
    def inc(xs: list):
        return (x + 1 for x in xs)

    @pipeliner(">>")
    def collapse(xs: list):
        return sum(xs)

    result = [1, 2, 3] >> inc >> double >> collapse

    assert result == 18
