"""
Extension methods for the 'statistics' library:
https://docs.python.org/3/library/statistics.html#module-statistics
"""


def multimode(data):
    """
    Quick implementation of the 'statistics.multimode' method introduced in Python 3.8:
    https://docs.python.org/3/library/statistics.html#statistics.multimode

    Return a list of the most frequently occurring values.
    Will return more than one result if there are multiple modes or an empty list if 'data' is empty.

    Usage:
    >>> multimode('aabbbbbbbbcc')
    ['b']
    >>> multimode('aabbbbccddddeeffffgg')
    ['b', 'd', 'f']
    >>> multimode('')
    []
    """
    if len(data) == 0:
        return []

    counts = {}
    for element in data:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

    max_count = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_count]
    if len(modes) > 1:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> multimode: multiple modes found - found {} modes: {}'.format(len(modes), modes))

    return modes

