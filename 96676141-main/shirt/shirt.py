import sys
import os
from PIL import Image, ImageOps

details = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.lower().endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid input")

    if not output_file.lower().endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid input")

    if not input_file.lower().endswith(output_file.lower().split(".")[-1]):
        sys.exit("Invalid input")

    image = Image.open(input_file)
    overlay_im = Image.open("shirt.png")
    size = overlay_im.size

    image = ImageOps.fit(image, (600,600), method=Image.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    image.paste(overlay_im, overlay_im)
    image.save(output_file)


