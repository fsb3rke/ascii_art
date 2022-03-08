from PIL import Image, ImageOps
from sys import argv

og_image = Image.open(argv[1])
gray_image = ImageOps.grayscale(og_image)
gray_image.save(f"{argv[2]}")