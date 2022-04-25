import argparse
import cv2
import numpy as np
from PIL import Image as PIL_Image

from maskrcnn_benchmark.config import cfg
from predictor import COCODemo


def main():
    print("Started")
    parser = argparse.ArgumentParser("Pytorch Object Detection")
    parser.add_argument(
        "--config-file",
        metavar="FILE",
        help="path to config file"
    )
    parser.add_argument(
        "--image-file",
        metavar="FILE",
        help="path to image file"
    )
    parser.add_argument(
        "--save-image",
        type=str,
        help="file name to store the processed image"
    )

    args = parser.parse_args()

    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(["MODEL.DEVICE", "cpu"])
    cfg.freeze()
    print(args.config_file)
    coco_demo = COCODemo(
        cfg,
        min_image_size=800,
        confidence_threshold=0.5,
    )

    pil_image = PIL_Image.open(args.image_file).convert("RGB")
    image = np.array(pil_image)[:, :, [2, 1, 0]]
    result_img, prediction_props = coco_demo.run_on_opencv_image(image, args)
    save_file = args.save_image
    cv2.imwrite(save_file, result_img)
    print(f"Result saved at: {save_file}")
    return list(prediction_props)

if __name__ == "__main__":
    main()

