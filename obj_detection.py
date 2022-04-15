import subprocess
import os

def exec_obj_detection():
    directory = 'inputdir'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            subprocess.call("python tools/demo/test_object_detection.py --config_file sgg_configs/vgattr/vinvl_x152c4.yaml --img_file " + f + " --save_file  output/" + os.path.split(f)[1] + ".obj.jpg MODEL.WEIGHT pretrained_model/vinvl_vg_x152c4.pth MODEL.ROI_HEADS.NMS_FILTER 1 MODEL.ROI_HEADS.SCORE_THRESH 0.2 TEST.IGNORE_BOX_REGRESSION False", shell=True)
