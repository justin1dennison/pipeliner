from pipeliner import __version__, pipeliner


def _square(x):
    return x * x


def _inc(x):
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
