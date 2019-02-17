"""
Strategies for picking a single edge to crop to from a list of edges along a scanline.

All methods take a list of edges as the first parameter and return the coordinates of one edge.
"""
import math


def first_edge(edges):
    """
    Return the coordinates of the first edge, or None if there are no edges.
    """
    try:
        return edges[0][1]
    except IndexError:
        return None


def last_edge(edges, depth=math.inf):
    """
    Return the coordinates of the deepest edge up to the depth, or None if no edges are within the depth.
    """
    coords_within_depth = [coord for index, coord in edges if index < depth]
    try:
        return coords_within_depth[-1]
    except IndexError:
        return None
