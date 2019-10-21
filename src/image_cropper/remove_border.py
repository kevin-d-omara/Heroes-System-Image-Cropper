from PIL import Image

from . import find_edges, pick_edge
from .scanline import get_scanlines_left_to_right, get_scanlines_right_to_left
from .scanline import get_scanlines_top_to_bottom, get_scanlines_bottom_to_top
from .statistics_extension import multimode


def remove_border(image: Image, get_edge_coordinates, num_scanlines=100, **kwargs):
    """
    Crop the image according to the strategy.

    :param image: The image to crop.
    :param get_edge_coordinates: TODO
    :param num_scanlines: Number of scanlines to distribute evenly along each edge.
    :param kwargs: Optional keyword arguments ``get_edge_coordinates`` takes.
    :return: Copy of the original image with the cropping applied.
    """
    # Get upper-left x-coordinate.
    scanlines = get_scanlines_left_to_right(image, num_lines=num_scanlines)
    edge_coords = get_edge_coordinates(image, scanlines, **kwargs)
    x_values = [coord[0] for coord in edge_coords]
    upper_left_x = min(multimode(x_values)) if len(x_values) > 0 else 0

    # Get upper-left y-coordinate.
    scanlines = get_scanlines_top_to_bottom(image, num_lines=num_scanlines)
    edge_coords = get_edge_coordinates(image, scanlines, **kwargs)
    y_values = [coord[1] for coord in edge_coords]
    upper_left_y = min(multimode(y_values)) if len(y_values) > 0 else 0

    # Get lower-right x-coordinate.
    scanlines = get_scanlines_right_to_left(image, num_lines=num_scanlines)
    edge_coords = get_edge_coordinates(image, scanlines, **kwargs)
    x_values = [coord[0] for coord in edge_coords]
    lower_right_x = max(multimode(x_values)) + 1 if len(x_values) > 0 else image.width

    # Get lower-right y-coordinate.
    scanlines = get_scanlines_bottom_to_top(image, num_lines=num_scanlines)
    edge_coords = get_edge_coordinates(image, scanlines, **kwargs)
    y_values = [coord[1] for coord in edge_coords]
    lower_right_y = max(multimode(y_values)) + 1 if len(y_values) > 0 else image.height

    bounding_box = (upper_left_x, upper_left_y, lower_right_x, lower_right_y)
    return image.crop(bounding_box)


def transparent_edge(image, scanlines):
    x_or_y_values = []
    for scanline in scanlines:
        edges = find_edges.where_non_transparent(image, scanline)
        edge = pick_edge.first_edge(edges)
        if edge is not None:
            x_or_y_values.append(edge)

    return x_or_y_values


def white_edge(image, scanlines):
    x_or_y_values = []
    for scanline in scanlines:
        edges = find_edges.where_non_white(image, scanline)
        edge = pick_edge.first_edge(edges)
        if edge is not None:
            x_or_y_values.append(edge)

    return x_or_y_values


def bad_pixels_edge(image, scanlines, crop_depth, search_depth):
    x_or_y_values = []
    for scanline in scanlines:
        edges = find_edges.where_color_changes(image, scanline, crop_depth=crop_depth, search_depth=search_depth)
        edge = pick_edge.last_edge(edges)
        if edge is None:
            x_or_y_values.append(scanline[0])
        else:
            x_or_y_values.append(edge)

    return x_or_y_values
