from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from a path an return an array of \
        the rgb value for each point."""
    assert isinstance(path, str), 'path is not a string'

    im = Image.open(path, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    imarray = np.array(pixel_values)
    imarray = imarray.reshape((height, width, 3))
    print("the shape of the array is: ", imarray.shape)
    return (imarray)
