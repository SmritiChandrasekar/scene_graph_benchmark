import subprocess
import os

def exec_obj_detection(model):
    directory = 'inputdir'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            subprocess.call("python main.py --config-file configs/" + model + " --image-file " + f + " --save-image  output/" + os.path.split(f)[1] + ".jpg." + os.path.split(model)[1] + ".obj.detected.jpg", shell=True)
