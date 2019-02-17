"""
Methods for operating on pixels of an image.

A pixel is a 4-tuple with channels ['R', 'G', 'B', 'A'], or a 3-tuple if missing the Alpha channel.
"""
import operator


def is_fully_transparent(pixel):
    return pixel[3] == 0


def is_partly_transparent(pixel):
    return pixel[3] < 255


def is_white(pixel):
    return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255


def has_alpha_channel(pixel):
    return len(pixel) == 4


def subtract(a, b):
    """
    Subtract one pixel from another. Subtracts each channel of `b` from `a``.
    """
    if len(a) != len(b):
        raise ValueError("Number of channels for pixel A and B do not match: " + str(len(b)) + " != " + str(len(b)))

    return tuple(map(operator.sub, a, b))


def get_intensity(pixel):
    """Return the combined value of all channels."""
    return sum(pixel)
