# Resizes image(s) by max_width.
#
# Usage:
#   python resize_image.py --image_dir="~/home/cche/image_dir/"

import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--image_dir',
                    help='The directory of images to resize')
parser.add_argument('--max_width', default=600, type=int,
                    help='The max width of the resized images')
args = parser.parse_args()

def resize_image():
    image_dir = os.path.abspath(args.image_dir)
    for filename in os.listdir(args.image_dir):
        path = os.path.join(args.image_dir, filename)
        if not os.path.isfile(path):
            print("skipped non-file path: ", path)
            continue
        # TODO: also skip non-image files

        image = Image.open(path)
        print("Read image: ", filename)
        height, width = image.size
        if width > args.max_width:
            resize_ratio = 1.0  * args.max_width / width
            resized_height = int(height * resize_ratio)
            image = image.resize((resized_height, args.max_width))
            image.save(path)
            print("Resized image: ", filename)

if __name__ == "__main__":
    resize_image()
