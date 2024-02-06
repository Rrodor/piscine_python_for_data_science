def square(x: int | float) -> int | float:
    """return the square of the variable"""
    return (x * x)


def pow(x: int | float) -> int | float:
    """return the variable exponent herself"""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """function that takes as argument a number and a function and returns
    an object that when called returns the result of the arguments calculation.
    """
    assert isinstance(x, (float, int)), "variable is not a valid number"

    count = 0

    def inner() -> float:
        nonlocal count
        res = function(x)
        for i in range(count):
            res = function(res)
        count += 1
        return res

    return inner
