from PIL import Image
import os
from shared import variables as var


def import_image(image_name, size):
    image = Image.open(os.path.join(var.images_dir, image_name))
    new_image = Image.new("RGBA", image.size, "WHITE")
    new_image.paste(image, (0, 0), image)
    return new_image.resize(size)


def save_image(image, name):
    image.save(os.path.join(var.images_dir, name))
