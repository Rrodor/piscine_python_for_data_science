import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2 dimensional array."""
    assert isinstance(family, list), 'family is not a list'
    assert isinstance(start, int), 'start is not an integer'
    assert isinstance(end, int), 'end is not an integer'

    arr = np.array(family)

    print("My shape is {}".format(arr.shape))
    arr = arr[start:end]
    print("My new shape is {}".format(arr.shape))
    return arr.tolist()
