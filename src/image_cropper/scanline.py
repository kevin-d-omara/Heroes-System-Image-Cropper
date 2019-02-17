"""
Methods to retrieve a scanline from an image. A scanline is a horizontal or vertical line of pixel coordinates.
"""
from PIL import Image
from typing import Tuple, List


def get_scanlines_left_to_right(image: Image, num_lines=1) -> List[List[Tuple[int, int]]]:
    """
    Return N scanlines spread evenly apart on the image's left side.

    For example,
        num_lines=1 => one line @ center of edge
        num_lines=2 => two lines @ 1/3 and 2/3 of edge
        num_lines=3 => three lines @ 1/4, 2/4, and 3/4
        etc.
    """
    return _get_scanlines(image, image.height, _get_scanline_left_to_right, num_lines=num_lines)


def get_scanlines_right_to_left(image: Image, num_lines=1) -> List[List[Tuple[int, int]]]:
    return _get_scanlines(image, image.height, _get_scanline_right_to_left, num_lines=num_lines)


def get_scanlines_top_to_bottom(image: Image, num_lines=1) -> List[List[Tuple[int, int]]]:
    return _get_scanlines(image, image.width, _get_scanline_top_to_bottom, num_lines=num_lines)


def get_scanlines_bottom_to_top(image: Image, num_lines=1) -> List[List[Tuple[int, int]]]:
    return _get_scanlines(image, image.width, _get_scanline_bottom_to_top, num_lines=num_lines)


def _get_scanlines(image: Image, length: int, get_scanline, num_lines=1) -> List[List[Tuple[int, int]]]:
    """
    :param length: The width or height of the image (to spread the scanlines across).
    :param get_scanline: One of the four ``_get_scanline_x_to_y`` methods below.
    """
    step_size = int(length / (num_lines + 1))
    scanlines = [
        get_scanline(image, fixed_value)
        for fixed_value in range(0, length+1, step_size)
    ]

    # Remove the first and last scanline. These are always the extreme top/bottom or left/right.
    return scanlines[1: -1]


def _get_scanline_left_to_right(image: Image, fixed_y_value: int) -> List[Tuple[int, int]]:
    """
    Return the coordinates of all pixels in a horizontal line moved left-to-right across the image.
    """
    return [(x_value, fixed_y_value) for x_value in range(0, image.width)]


def _get_scanline_right_to_left(image: Image, fixed_y_value: int) -> List[Tuple[int, int]]:
    return [(x_value, fixed_y_value) for x_value in range(image.width - 1, 0, -1)]


def _get_scanline_top_to_bottom(image: Image, fixed_x_value: int) -> List[Tuple[int, int]]:
    return [(fixed_x_value, y_value) for y_value in range(0, image.height)]


def _get_scanline_bottom_to_top(image: Image, fixed_x_value: int) -> List[Tuple[int, int]]:
    return [(fixed_x_value, y_value) for y_value in range(image.height - 1, 0, -1)]
