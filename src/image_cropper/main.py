"""
Entry point to the Heroes System Image Cropper program.
"""
import sys
import os
from pathlib import Path

from PIL import Image
from image_cropper.remove_border import remove_border, transparent_edge, white_edge, bad_pixels_edge
from image_cropper.image_extensions import has_alpha_channel
from image_cropper import _hardcode

OUTPUT_FOLDER = Path('cropped')


def main():
    """
    Crop all the named images (argv[1:]) and save them to a new directory "./cropped/".
    """
    sys.argv[1] = _hardcode.get_image_path(_hardcode.HOUSE_WITH_VARIETY, _hardcode.BASE)
    print("Running HeroesSystemImageCropper")
    print("Working Directory: " + os.getcwd())
    print("Output Directory: " + str(Path(os.getcwd()).joinpath(OUTPUT_FOLDER)))
    print("Args: " + str(sys.argv[1:]))

    file_names = sys.argv[1:]
    image_paths = [try_create_path(name) for name in file_names]
    original_images = [Image.open(path) for path in image_paths]
    cropped_images = [crop_image(image) for image in original_images]

    OUTPUT_FOLDER.mkdir(exist_ok=True)
    for image, path in zip(cropped_images, image_paths):
        save_image(image, OUTPUT_FOLDER.joinpath(path.name))


def try_create_path(file_name: str) -> Path:
    path = Path(file_name)
    if not path.exists():
        raise ValueError("File does not exist: " + str(path))
    print("Found image " + str(path))
    return path


def crop_image(image: Image) -> Image:
    if has_alpha_channel(image):
        # Remove transparency from each side.
        image = remove_border(image, transparent_edge, num_scanlines=100)
    else:
        # Remove white from each side. White is like transparency for images without an alpha channel.
        image = remove_border(image, white_edge, num_scanlines=100)
    log_image(image, "transparency")

    # Remove blurred pixels from each side to make the colors crisp.
    kwargs = {
        "crop_depth": 5,
        "search_depth": 15,
    }
    image = remove_border(image, bad_pixels_edge, num_scanlines=100, **kwargs)
    log_image(image, "fuzzy pixels")

    return image


def save_image(image: Image, relative_path: Path) -> None:
    print("Saving cropped image to: " + str(relative_path))
    image.save(relative_path)
    # print("    with width and height: (" + str(image.width) + ", " + str(image.height) + ")")


def log_image(image: Image, filter_name: str) -> None:
    print("After removing " + filter_name + ":")
    print("    width and height: (" + str(image.width) + ", " + str(image.height) + ")")


if __name__ == "__main__":
    main()
