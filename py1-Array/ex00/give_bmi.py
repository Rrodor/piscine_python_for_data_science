import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    try:
        assert len(height) == len(weight), \
            "height and weight must have the same length"
        assert all(isinstance(h, (int, float)) for h in height), \
            "height must be a list of int or float"
        assert all(isinstance(w, (int, float)) for w in weight), \
            "weight must be a list of int or float"
    except AssertionError as e:
        print("AssertionError: {}".format(e))
        return []
    return list(np.array(weight) / np.array(height) ** 2)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    try:
        assert all(isinstance(b, (int, float)) for b in bmi), \
            "bmi must be a list of int or float"
        assert isinstance(limit, int), \
            "limit must be an int"
    except AssertionError as e:
        print("AssertionError: {}".format(e))
        return []
    return list(np.array(bmi) > limit)
