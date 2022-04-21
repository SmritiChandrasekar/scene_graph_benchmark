import json

def cal_iou(original_img, transformed_img):
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
        for trans_obj in transformed_img:
            if obj'label'] == trans_obj['label']:
                label_count = label_count+1
                boxA = obj['bounding_box']
                boxB = trans_obj['bounding_box']
                iou_sum = iou_sum + calculate_iou(boxA, boxB)
    return(iou_sum/label_count)

def calculate_iou(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    iou = interArea / float(boxAArea + boxBArea - interArea)

    print(iou)
    return(iou)
