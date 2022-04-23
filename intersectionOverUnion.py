import json
import torch
import torchvision.ops.boxes as bops

def calculate_iou(original_img, transformed_img):
   # f = open('detection_output.json')
   # data = json.load(f)
   # images = data['category']
   # img1 = images[0]
   # pic1 = img1['woman_fish'][0]
   # img2 = images[1]
   # pic2 = img2['woman_fish'][0]
    label_count=0
    iou_sum=0
    for obj in original_img:
        closest_iou = 0
        for trans_obj in transformed_img:
            if obj["label"] == trans_obj["label"]:
                #print(obj["label"])
                boxA = obj["bounding_box"]
                boxB = trans_obj["bounding_box"]
                #print(boxA)                                                                 
                #print(boxB)
                iou = calculateBboxIOU(boxA, boxB)
                if(iou > closest_iou):
                    closest_iou = iou
        #print(closest_iou)
        if closest_iou > 0.4:
            label_count = label_count + 1
            iou_sum = iou_sum + closest_iou
    if label_count > 0 :
        print("iou metrics: ")
        print(iou_sum/label_count)
        return(iou_sum/label_count)
    return 0

def calculateBboxIOU(bbox1, bbox2):
    box1 = torch.tensor([bbox1], dtype=torch.float)
    box2 = torch.tensor([bbox2], dtype=torch.float)
    iou = bops.box_iou(box1, box2)

    #print(iou.item())
    return iou.item()

