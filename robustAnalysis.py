from image_transformer import img_transformer
from obj_detection import exec_obj_detection
import os
import json

def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.loads(file.read())
        print(file_data)
        # Join new_data with file_data inside emp_details
        file_data["metrics"].append(new_data)
        print(file_data)
        # Sets file's current position at offset.
        file.seek(0)
    
        # convert back to json.
        json.dump(file_data, file, indent = 4)


original_list = img_transformer()
exec_obj_detection()

transformations = ["_rotated_image.jpg","_horizontal_flip_image.jpg", "_vertical_flip_image.jpg", "_guassian_noise_image.jpg","_median_noise_image.jpg","_grey_scale_image.jpg"]
f = open('detection_output.json')
obj_detection_data = json.load(f)
output_json = {}
for img in original_list:
    for i in obj_detection_data['category']:                                
        for key, value in i.items():                                        
            if key == img:
                original_img_ouput = value
    metrics_list = []   
    for transformation in transformations:
        filename = img + transformations 
        image_name, file_extension = os.path.splitext(img)
        for i in obj_detection_data['category']:
            for key, value in i.items():
                if key == image_name:
                    average_predicted_label = calculate_label_metrics(original_img_ouput, value)
                    apply_bbox_transformations(transformation, value)
                    average_iou = calculate_iou(original_img_ouput, value)
                    metrics = {}
                    key_value_pair = {}
                    metrics["average_predicted_label"]= average_predicted_label
                    metrics["average_iou"] = average_iou
                    key_value_pair[image_name] = metrics
                    metrics_list.append(key_value_pair)

    output_json["img"] = metrics_list
    text_save_file = 'metrics_output.json'
    write_json(output_json, text_save_file)
#json written in file



