IMAGES_ROOT = '../../test/images'

BASE = 'image.png'
CROP_1 = 'image-crop-1.png'
CROP_2 = 'image-crop-1.png'


# Images with all states:
BUILDING_BREACH = 'building-breach'
HOUSE_WITH_GAP = 'house-with-gap'
HOUSE_WITH_VARIETY = 'house-with-variety'
M8_SCOUT = 'm8-scout'
M8_SCOUT_BACKSIDE = 'm8-scout-backside'
PANZERSHRECK = 'panzershreck'
SUPPRESSION = 'suppression'


def get_image_path(*args):
    return '/'.join([IMAGES_ROOT, *args])
