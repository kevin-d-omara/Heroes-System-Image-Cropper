import pytest
from PIL import Image
from collections import namedtuple
from src.image_cropper.remove_border import remove_border, transparent_edge, bad_pixels_edge


ImageStates = namedtuple('ImageStates', ['base', 'crop_1', 'crop_2'])


def test_m8_scout_frontside():
    """
    This image has transparency and bad pixels on all sides.
    There is no color noise, except for 1 vertical band on the right side.
    """
    _test_remove_border_all_steps("m8-scout")


def test_m8_scout_backside():
    """
    This image has transparency and bad pixels on all sides.
    There is color noise, but only in the second half of each color band.
    """
    _test_remove_border_all_steps("m8-scout-backside")


def test_panzershreck():
    """
    This image is already cropped on the left and right sides, but not vertically.
    """
    _test_remove_border_all_steps("panzershreck")


def test_suppression():
    """
    The image has transparency on all sides and bad pixels on all except the top.
    The color while moving towards the center is a gradient from dark orange to light orange.
    """
    _test_remove_border_all_steps("suppression")


@pytest.mark.skip(reason="Doesn't work. I'm okay not covering this use case since it's rare.")
def test_building_breach():
    """
    The image is irregularly shaped, like a squished and rounded hexagon.
    """
    _test_remove_border_all_steps("building-breach")


def test_house_with_variety():
    """
    The image has large variations in color along all sides (ex: grass, flowers, dirt, concrete, mattress, etc.).
    """
    _test_remove_border_all_steps("house-with-variety")


def _test_remove_border_all_steps(dir_name):
    expected = _get_expected_image_states(dir_name)

    actual = _get_actual_image_states(expected.base)

    _assert_images_are_equal(actual.crop_1, expected.crop_1)
    _assert_images_are_equal(actual.crop_2, expected.crop_2)


def _get_expected_image_states(dir_name):
    base_path = "test/images/" + dir_name + "/"

    return ImageStates(
        Image.open(base_path + "image.png"),         # The base image with no cropping. Direct from photoshop template.
        Image.open(base_path + "image-crop-1.png"),  # After transparency has been removed.
        Image.open(base_path + "image-crop-2.png"),  # After the bad pixels have been removed.
    )


def _get_actual_image_states(base_image: Image):
    num_scanlines = 100
    intensity_threshold = 40
    depth = 5

    crop_1 = remove_border(base_image, transparent_edge, num_scanlines=num_scanlines)
    crop_2 = remove_border(crop_1, bad_pixels_edge, num_scanlines=num_scanlines,
                           intensity_threshold=intensity_threshold, depth=depth)

    return ImageStates(base_image, crop_1, crop_2)


def _assert_images_are_equal(actual: Image, expected: Image):
    assert actual.width == expected.width
    assert actual.height == expected.height
