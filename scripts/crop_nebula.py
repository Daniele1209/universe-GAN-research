
DIR = 'E:/DATA/Nebulae/train'
OUT_DIR = 'E:/DATA/Nebulae/train-crop/'

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
                pad_tb = (img_width - img_height) // 2
                pad_lr = 0
            else:
                pad_tb = 0
                pad_lr = (img_height - img_width) // 2

            cropped_img = cv2.copyMakeBorder(img, pad_tb, pad_tb, pad_lr, pad_lr, cv2.BORDER_REPLICATE)

            # check if we lose a pixel when dividing
            # and pad again by one pixel
            img_height, img_width, channels = cropped_img.shape
            if img_height > img_width:
                cropped_img = cv2.copyMakeBorder(cropped_img, 0, 0, img_height-img_width, 0, cv2.BORDER_REPLICATE)
            elif img_width > img_height:
                cropped_img = cv2.copyMakeBorder(cropped_img, img_width-img_height, 0, 0, 0, cv2.BORDER_REPLICATE)

            # debug visualizer
            # img_height, img_width, channels = cropped_img.shape
            # print('Height: ' + str(img_height))
            # print('Width: ' + str(img_width))
            # cv2.imshow('cropped', cropped_img)
            # cv2.waitKey(0)

            # save image to output dir
            cv2.imwrite(OUT_DIR+image_path, cropped_img)

    print(invalid_list)