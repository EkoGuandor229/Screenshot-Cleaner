from PIL import Image
import numpy as np




def getpositionoffirstblackpixelinrange(image, start, stop, step):
    for x in range(start, stop, step):
        if image.getpixel((1, x)) >= (5, 5, 5):
            return x



image = Image.open("Unbearbeitete Bilder/Screenshot_20200826-113200.jpg")


def crop_image(image):
    global cropped_image
    upper_crop_level = getpositionoffirstblackpixelinrange(image, 0, image.size[1], 1)
    lower_crop_level = getpositionoffirstblackpixelinrange(image, image.size[1] - 1, 0, -1)
    box = (0, upper_crop_level, image.size[0], lower_crop_level)
    return image.crop(box)


cropped = crop_image(image)
cropped.show()





# 1. Load all images
# 2. For each image From Top to bottom:
#   Check the leftmost rightmost and middle pixel
#   If l == r == m != Black -> get pixel position
#   Crop pixel at that position
# 3. From Bottom to Top -> same procedure