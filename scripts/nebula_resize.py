from PIL import Image
import os, sys

input_images_path = "E:/DATA/Nebulae/train-crop/"
output_images_path = "E:/DATA/Nebulae/downscaled-crop-512/"
dirs = os.listdir(input_images_path)

for item in dirs:
    if os.path.isfile(input_images_path+item):
        im = Image.open(input_images_path+item)
        f, e = os.path.splitext(input_images_path+item)
        imResize = im.resize((512, 512), Image.ANTIALIAS)
        imResize.save(output_images_path + f.split('/')[-1] + '.jpg', 'JPEG', quality=90)