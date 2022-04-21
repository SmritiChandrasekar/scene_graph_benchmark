import cv2
import os

def img_transformer():
    dir_path = r'original_images_dir'
    img_list = os.listdir(dir_path)

    for img in img_list:
        path = r'original_images_dir/'+img
        filename, file_extension = os.path.splitext(img)
        # Reading an image in default mode
        src = cv2.imread(path)
        rotated_image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
        horizontal_flip_image=cv2.flip(src, 1)
        vertical_flip_image=cv2.flip(src, 0)
        rotated_image_filename = 'inputdir/' + filename + '_rotated_image.jpg'
        horizontal_fliename='inputdir/' + filename + '_horizontal_flip_image.jpg'
        vertical_fliename='inputdir/' + filename + '_vertical_flip_image.jpg'
        guassian_noise_filename='inputdir/' + filename + '_guassian_noise_image.jpg'
        median_noise_filename='inputdir/' + filename + '_median_noise_image.jpg'
        grey_scale_filename='inputdir/' + filename + '_grey_scale_image.jpg'
        #Creating Noise images
        #Gaussian Blur
        gausBlur = cv2.GaussianBlur(src, (51,51),0)
        medBlur = cv2.medianBlur(src,51)
        grayscale_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
   

        # Using cv2.imwrite() method
        # Saving the image
        cv2.imwrite('inputdir/' + img, src)
        cv2.imwrite(rotated_image_filename, rotated_image)
        cv2.imwrite(horizontal_fliename, horizontal_flip_image)
        cv2.imwrite(vertical_fliename, vertical_flip_image)
        cv2.imwrite(guassian_noise_filename,gausBlur)
        cv2.imwrite(median_noise_filename,medBlur)
        cv2.imwrite(grey_scale_filename,grayscale_img)
    return img_list
