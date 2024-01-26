import numpy as np
from matplotlib import pyplot as plt


def ft_invert(array) -> np.array:
    """Invert the color of an image."""
    assert isinstance(array, np.ndarray), 'array is not a np.array'

    arr = 255 - array.copy()
    plt.imshow(arr)
    plt.axis('off')
    plt.show()
    return (arr)


def ft_red(array) -> np.array:
    """Keep only the red color of an image."""
    assert isinstance(array, np.ndarray), 'array is not a np.array'

    arr = array.copy()
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    plt.imshow(arr)
    plt.axis('off')
    plt.show()
    return (arr)


def ft_green(array) -> np.array:
    """Keep only the green color of an image."""
    assert isinstance(array, np.ndarray), 'array is not a np.array'

    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    plt.imshow(arr)
    plt.axis('off')
    plt.show()
    return (arr)


def ft_blue(array) -> np.array:
    """Keep only the blue color of an image."""
    assert isinstance(array, np.ndarray), 'array is not a np.array'

    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    plt.imshow(arr)
    plt.axis('off')
    plt.show()
    return (arr)


def ft_grey(array) -> np.array:
    """Transform an image to grey scale."""
    assert isinstance(array, np.ndarray), 'array is not a np.array'

    arr = array.copy()
    arr[:, :, 0] = arr[:, :, 0] / 3.344
    arr[:, :, 1] = arr[:, :, 1] / 1.704
    arr[:, :, 2] = arr[:, :, 2] / 8.772
    arr = arr.sum(axis=2)
    plt.imshow(arr)
    plt.imshow(arr, cmap='gray')
    plt.axis('off')
    plt.show()
    return (arr)
