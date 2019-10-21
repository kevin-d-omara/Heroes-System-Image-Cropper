from src.image_cropper import statistics_extension


def test_multimode_single_mode():
    # Arrange
    data = 'aabbbbbbbbcc'

    # Act
    modes = statistics_extension.multimode(data)

    # Assert
    assert len(modes) == 1
    assert modes[0] == 'b'


def test_multimode_multiple_modes():
    # Arrange
    data = 'aabbbbccddddeeffffgg'
    expected_modes = ['b', 'd', 'f']

    # Act
    modes = statistics_extension.multimode(data)

    # Assert
    assert 3 == len(modes)
    for expected, actual in zip(expected_modes, modes):
        assert actual == expected


def test_multimode_empty_data():
    # Arrange
    data = []

    # Act
    modes = statistics_extension.multimode(data)

    # Assert
    assert 0 == len(modes)
