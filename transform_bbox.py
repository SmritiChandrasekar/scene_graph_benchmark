import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image as PIL_Image
import numpy as np
import cv2
import torch
import torchvision.ops.boxes as bops
import json

def apply_bbox_transformations(transformation, image_path, json_data):
    img = np.array(PIL_Image.open(image_path))
    bboxes = np.array([obj['bounding_box'] for obj in json_data])
    if transformation == "_horizontal_flip_image.jpg" :
        return(flip_horizontal_bboxes(img, bboxes))
    if transformation == "_vertical_flip_image.jpg" :                         
        return(flip_vertical_bboxes(img, bboxes))
    return([],[])

def flip_horizontal_bboxes(img, bboxes):
    img_center = np.array(img.shape[:2])[::-1]/2
    img_center = np.hstack((img_center, img_center))
    img =  img[:,::-1,:]
    bboxes[:,[0,2]] += 2*(img_center[[0,2]] - bboxes[:,[0,2]])
    box_w = abs(bboxes[:,0] - bboxes[:,2])
    bboxes[:,0] -= box_w
    bboxes[:,2] += box_w
    return img, bboxes

def flip_vertical_bboxes(img, bboxes):
    img_center = np.array(img.shape[:2])[::-1]/2
    img_center = np.hstack((img_center, img_center))
    img =  img[::-1,:,:]
    bboxes[:,[1,3]] += 2*(img_center[[1,3]] - bboxes[:,[1,3]])
    box_h = abs(bboxes[:,1] - bboxes[:,3])
    bboxes[:,1] -= box_h
    bboxes[:,3] += box_h
    return img, bboxes


