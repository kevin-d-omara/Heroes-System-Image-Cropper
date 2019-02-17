from src.image_cropper import pixel


def test_subtract():
    a = (5, 1, 500, -15)
    b = (2, 6, 1, -16)

    c = pixel.subtract(a, b)

    assert c == (3, -5, 499, 1)


def test_get_intensity():
    px = (1, 2, 3, 4)

    intensity = pixel.get_intensity(px)

    assert intensity == px[0] + px[1] + px[2] + px[3]
