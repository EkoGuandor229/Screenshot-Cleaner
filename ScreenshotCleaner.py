from PIL import Image
import glob


def getpositionoffirstblackpixelinrange(image, start, stop, step):
    for x in range(start, stop, step):
        if image.getpixel((1, x)) >= (5, 5, 5):
            return x
        elif image.getpixel((image.size[0]-1, x)) >= (5, 5, 5):
            return x


def crop_image(image):
    upper_crop_level = getpositionoffirstblackpixelinrange(image, 0, image.size[1], 1)
    lower_crop_level = getpositionoffirstblackpixelinrange(image, image.size[1] - 1, 0, -1)
    box = (
        0,
        upper_crop_level,
        image.size[0]-1,
        lower_crop_level
    )
    return image.crop(box)


for file in glob.glob("Unbearbeitete Bilder/*.jpg"):
    image_name = file[21:]
    image = Image.open(file)
    cropped = crop_image(image)
    cropped.save("Korrigierte Bilder/" + image_name)
    print(image_name)