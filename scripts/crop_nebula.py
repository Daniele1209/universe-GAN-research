import cv2
import numpy as np
import os

DIR = 'D:/DATA/train'
OUT_DIR = 'D:/DATA/Nebulae/train-crop/'

if __name__ == '__main__':
    invalid_list = []
    for image_path in os.listdir(DIR):

        is_valid = True
        img = cv2.imread(DIR + '/' + image_path)
        try:
            img_height, img_width, channels = img.shape
        except Exception:
            invalid_list.append(image_path)
            is_valid = False
        if is_valid:
            # check if the max length is img width or height
            max_val = max(img_width, img_height)
            if max_val == img_width:
                mid_point = img_width // 2
                cropped_image = img[0:img_height, mid_point-img_height//2:mid_point+img_height//2]
            else:
                mid_point = img_height // 2
                cropped_image = img[mid_point - img_width // 2:mid_point + img_width // 2, 0:img_width]

            # check if we lose a pixel when dividing
            # and pad again by one pixel
            img_height, img_width, channels = cropped_image.shape
            if img_height > img_width:
                cropped_image = cv2.copyMakeBorder(cropped_image, 0, 0, img_height-img_width, 0, cv2.BORDER_REPLICATE)
            elif img_width > img_height:
                cropped_image = cv2.copyMakeBorder(cropped_image, img_width-img_height, 0, 0, 0, cv2.BORDER_REPLICATE)

            # debug visualizer
            # img_height, img_width, channels = cropped_image.shape
            # print('Height: ' + str(img_height))
            # print('Width: ' + str(img_width))
            # cv2.imshow('cropped', cropped_image)
            # cv2.waitKey(0)

            # save image to output dir
            cv2.imwrite(OUT_DIR+image_path, cropped_image)

    print(invalid_list)