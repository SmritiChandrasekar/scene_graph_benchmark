import json

f = open('detection_output.json')
data = json.load(f)
images = data['category']
img1 = images[0]
pic1 = img1['woman_fish'][0]
img2 = images[1]
pic2 = img2['woman_fish'][0]
boxA = pic1['bounding_box']
boxB = pic2['bounding_box']

xA = max(boxA[0], boxB[0])
yA = max(boxA[1], boxB[1])
xB = min(boxA[2], boxB[2])
yB = min(boxA[3], boxB[3])

interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

iou = interArea / float(boxAArea + boxBArea - interArea)

print(iou)
