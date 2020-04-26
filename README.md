# pipeliner


Let's abuse Python magic methods to compose some functions. Let's see what I mean.

```python

from pipeliner import pipeliner

@pipeliner(">>")
def square(x):
    return x * x

@pipeliner(">>"):
def inc(x):
    return x + 1

@pipeliner(">>"):
def cube(x):
    return x ** 3


tally = (2 >> square >> inc >> cube)
assert tally == 125
```

Now there are some shortcomings to this current solution:
- The operators can only be "|", "^", and ">>".
- The functions that are decorated can only take a single parameter as that dictates how the values progress through the pipeline.