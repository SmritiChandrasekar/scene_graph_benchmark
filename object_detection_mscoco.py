import subprocess
import os

def exec_obj_detection():
    directory = 'inputdir'
    model = "caffe2/e2e_faster_rcnn_X_101_32x8d_FPN_1x_caffe2.yaml"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            subprocess.call("python main.py --config-file configs/" + model + " --image-file " + f + " --save-image  output/" + os.path.split(f)[1] + ".jpg." + os.path.split(model)[1] + ".obj.detected.jpg", shell=True)
