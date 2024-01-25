from matplotlib import pyplot as plt
from load_image import ft_load
import numpy as np


def slice_me2d(arr: np.array, start1, end1, start2, end2) -> np.array:
    """Slice a 2 dimensional array."""
    # assert isinstance(family, list), 'family is not a list'
    assert isinstance(start1, int), 'start1 is not an integer'
    assert isinstance(end1, int), 'end2 is not an integer'
    assert isinstance(start2, int), 'start2 is not an integer'
    assert isinstance(end2, int), 'end2 is not an integer'

    arr = arr[start1:end1, start2:end2, 1]
    return arr


def ft_zoom(arr: np.array, factor: int, posx: int, posy: int) -> np.array:
    """ zoom an image by factor """
    assert isinstance(factor, int), 'factor is not an integer'

    arr = slice_me2d(arr, factor + posx, posx + arr.shape[0] - factor,
                     factor + posy, posy + arr.shape[0] - factor)
    return arr


def main():
    """program that print a black and white and zoomed version of an image."""
    arr = ft_load("animal.jpeg")
    print(arr)
    arr = ft_zoom(arr, 184, -85, 270)
    arr = arr.reshape((arr.shape[0], arr.shape[1], 1))
    height = arr.shape[0]
    width = arr.shape[1]
    print("the shape of the array is: ", arr.shape,
          "or ({}, {})".format(height, width))
    print(arr)
    plt.imshow(arr, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
