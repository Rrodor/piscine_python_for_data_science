import numpy as np


def ft_mean(args: any) -> float:
    """print the mean of the given arguments"""
    mean = sum(args) / len(args)
    return mean


def ft_median(args: any) -> float:
    """print the median of the given arguments"""
    indexMedian = int(len(args) / 2)
    median = args[indexMedian]
    return median


def ft_quartile(args: any) -> list:
    """print the first and the third quartile of the given arguments"""
    quartile25 = float(args[int(len(args)/4)])
    quartile75 = float(args[int(3 * len(args)/4)])
    quartile = [quartile25, quartile75]
    return quartile


def ft_std(args: any) -> float:
    """print the standart deviation of the given arguments"""
    var = ft_var(args)
    std = np.sqrt(var)
    return std


def ft_var(args: any) -> float:
    mean = ft_mean(args)
    var = sum([np.power((x - mean), 2) for x in args]) / len(args)
    return var


def ft_statistics(*args: any, **kwargs: any) -> None:
    """print statistics of the given arguments"""

    assert (all(isinstance(item, (int, float)) for item in args)), \
        "the number given are not valid"
    validkeys = ["mean", "median", "quartile", "std", "var"]

    nums = list(args)
    nums.sort()
    for key, value in kwargs.items():
        value = value.lower()
        for validkey in validkeys:
            if value == validkey:
                if len(args) == 0:
                    print("ERROR")
                else:
                    match validkey:
                        case "mean":
                            print(f"mean : {ft_mean(nums)}")
                        case "median":
                            print(f"median : {ft_median(nums)}")
                        case "quartile":
                            print(f"quartile : {ft_quartile(nums)}")
                        case "std":
                            print(f"std : {ft_std(nums)}")
                        case "var":
                            print(f"var : {ft_var(nums)}")
