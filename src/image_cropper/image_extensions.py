"""
Extension methods for working with Images from the Pillow library:
https://pillow.readthedocs.io/en/stable/index.html
"""
from .pixel import has_alpha_channel as has_alpha


def has_alpha_channel(image):
    upper_left_pixel = image.getpixel((0, 0))
    return has_alpha(upper_left_pixel)
