from image_transformer import img_transformer
from obj_detection import exec_obj_detection
from transform_bbox import apply_bbox_transformations
from intersectionOverUnion import calculate_iou
import os
import json
def write_avg_json(new_data, filename):
    with open(filename,'r+') as file:                                           
          # First we load existing data into a dict.                            
        file_data = json.loads(file.read())                                     
        #print(file_data)                                                       
        # Join new_data with file_data inside emp_details                       
        file_data["total_average"].append(new_data)                                   
        print("Writing file data: ")
        print(file_data)                                
        # Sets file's current position at offset.                               
        file.seek(0)                                                            
                                                                                
        # convert back to json.                                                 
        json.dump(file_data, file, indent = 4)

def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.loads(file.read())
        #print(file_data)
        # Join new_data with file_data inside emp_details
        file_data["metrics"].append(new_data)
        print("Writing file data: ")
        print(file_data)
        # Sets file's current position at offset.
        file.seek(0)
    
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def calculate_label_metrics(original_img, transformed_img):
    og_label_list = []
    flip_label_list =[]
    for label in original_img:
        og_label_list.append(label["label"])
    print("original image label list: ")
    print(og_label_list)
    for labeltn in transformed_img:                                                  
        flip_label_list.append(labeltn["label"])
    print("flipped image label list:")
    print(flip_label_list)
    common_elements = list(set(og_label_list).intersection(set(flip_label_list)))
    union_list = list(set(og_label_list) | set(flip_label_list))
    print("label metrics: ")
    print(len(common_elements)/len(union_list))
    return(len(common_elements)/len(union_list))

original_list = img_transformer()
exec_obj_detection()

transformations = ["_rotated_image.jpg","_horizontal_flip_image.jpg", "_vertical_flip_image.jpg", "_guassian_noise_image.jpg","_median_noise_image.jpg","_grey_scale_image.jpg"]
f = open('detection_output.json')
obj_detection_data = json.load(f)
output_json = {}
original_img_ouput=[]
tot_avg_iou=[0,0,0,0,0,0]
tot_avg_labels=[0,0,0,0,0,0]
index=-1
for img_file in original_list:
    img, file_extension = os.path.splitext(img_file)
    found_img = 0
    for i in obj_detection_data['category']:
        print(i)                                
        for key, value in i.items(): 
            #print(key)
            #print(img)
            #print("searching..")                                       
            if key == img:
                found_img = 1
                original_img_ouput = value
                print("original image: ")
                print(key)
                break
        if found_img == 1:
            break
    metrics_list = []    
    for transformation in transformations:
        index = index + 1
        filename = img + transformation 
        image_name, file_extension = os.path.splitext(filename)
        found = 0
        for i in obj_detection_data['category']:
            for key, value in i.items(): 
                if key == image_name:
                    found = 1
                    print("transformed image: ")
                    print( key)
                    average_predicted_label = calculate_label_metrics(original_img_ouput, value)
                    tot_avg_labels[index] = tot_avg_labels[index] + average_predicted_label
                    if transformation == "_horizontal_flip_image.jpg" or transformation ==  "_vertical_flip_image.jpg":
                        newimg, new_bboxes = apply_bbox_transformations(transformation, "inputdir/" + filename, value)
                        print("before bbox transformation: ")
                        print(value)
                        for b in range(new_bboxes.shape[0]):
                            value[b]["bounding_box"] = new_bboxes[b].tolist()
                        print("updated value:")
                        print(value)
                    average_iou = calculate_iou(original_img_ouput, value)
                    tot_avg_iou[index] = tot_avg_iou[index] + average_iou
                    metrics = {}
                    key_value_pair = {}
                    metrics["average_predicted_label"]= average_predicted_label
                    metrics["average_iou"] = average_iou
                    key_value_pair[image_name] = metrics
                    metrics_list.append(key_value_pair)
                    break
            if found == 1:
                break
    output_json[img] = metrics_list
    text_save_file = 'metrics_comparison.json'
    write_json(output_json, text_save_file)
avg_json = {}
for t in range(6):
    temp = {}
    temp["tot_avg_labels"] = tot_avg_labels[t]
    temp["tot_avg_iou"] = tot_avg_iou[t]
    avg_json[transformations[t]] = temp
write_avg_json(avg_json, text_save_file)
#json written in file



