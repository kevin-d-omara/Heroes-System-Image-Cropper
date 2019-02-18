"""
Strategies for finding edges along a scanline.

All methods return a nested tuple of (index, (x, y)) for each pixel identified as an "edge".

The edge pixels are always on the "other side of the fence".
If used for cropping, all pixels in the scanline before this pixel should be cropped out.
"""
from . import pixel
from .itertools_extensions import window


def where_color_changes(image, scanline, crop_depth=5, search_depth=15):
    """
    Return the coordinates of each pixel where the previous pixel is a different color.

    Two pixels are a different color if the difference in their intensity is above the ``intensity_threshold``.
    """
    pixels = [image.getpixel(coord) for coord in scanline]
    transition_intensities = [
        abs(pixel.get_intensity(pixel.subtract(adjacent_px[0], adjacent_px[1])))
        for adjacent_px
        in window(pixels, n=2)
    ]

    crop_intensities = transition_intensities[0:crop_depth]
    search_intensities = transition_intensities[crop_depth:search_depth]
    intensity_threshold = max(search_intensities)

    return [
        (index + 1, coord)
        for index, (intensity, coord) in enumerate(zip(crop_intensities, scanline[1:]))
        if intensity > intensity_threshold
    ]


def where_non_transparent(image, scanline):
    """
    Return the coordinates of each opaque pixel (alpha=255).
    """
    return where_false(image, scanline, pixel.is_partly_transparent)


def where_non_white(image, scanline):
    """
    Return the coordinates of each white pixel (R=G=B=255).
    """
    return where_false(image, scanline, pixel.is_white)


def where_false(image, scanline, boolean_condition):
    """
    Return the coordinates of all pixels not matching the condition.

    :param boolean_condition: A function which takes a pixel (3-tuple or 4-tuple) and returns True or False.
    """
    return [
        (index, coord)
        for index, coord
        in enumerate(scanline)
        if not boolean_condition(image.getpixel(coord))
    ]
