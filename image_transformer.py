import cv2
import os

def img_transformer():
    dir_path = r'inputdir'
    img_list = os.listdir(dir_path)

    for img in img_list:
        path = r'inputdir/'+img
  
        # Reading an image in default mode
        src = cv2.imread(path)
        rotated_image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
        horizontal_flip_image=cv2.flip(src, 1)
        vertical_flip_image=cv2.flip(src, 0)
        rotated_image_filename = 'inputdir/' + img + '_rotated_image.jpg'
        horizontal_fliename='inputdir/' + img + '_horizontal_flip_image.jpg'
        vertical_fliename='inputdir/' + img + '_vertical_flip_image.jpg'
        # Using cv2.imwrite() method
        # Saving the image
        cv2.imwrite(rotated_image_filename, rotated_image)
        cv2.imwrite(horizontal_fliename, horizontal_flip_image)
        cv2.imwrite(vertical_fliename, vertical_flip_image)
    return img_list
