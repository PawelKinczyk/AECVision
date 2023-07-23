from pathlib import Path
import fitz
import glob
from PIL import Image
import io

import torch
import numpy as np
import pandas as pd
import shutil
import os
import json

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

# from custom_yolo_model_for_sahi import COTSYolov5DetectionModel
CUSTOM_YOLO5_CLASS = True


def to_1280_format(h, w):
    # Return pixel numbers for crop
    return ((w - 1) * 1280, (h - 1) * 1280, w * 1280, h * 1280)


class Convert_pdf:
    def __init__(self, path_pdf):
        self.path_pdf = path_pdf

        self.pdf_list = list(self.path_pdf.glob("**/*.pdf"))

        if not self.pdf_list:
            raise FileNotFoundError("No PDF files found in the specified path.")
        self.doc = fitz.open(self.pdf_list[0])
        self.page = self.doc.load_page(0)
        self.pixmap = self.page.get_pixmap(dpi=300)
        # convert_pdf = path_convert_pdf / "{0}.jpg".format(pdf_list[0].name)
        # pixmap.save(convert_pdf)

    def return_pixmap(self):
        return self.pixmap.tobytes("jpg")

    def return_image(self):
        return Image.open(io.BytesIO(self.pixmap))

    def save_image(self, export_path):
        export_path = path_convert_pdf / "{0}.jpg".format(self.pdf_list[0].name)
        self.pixmap.save(export_path)
        return export_path


def crop_image(
    path_pdf,
    path_convert_pdf,
    bytes_image,
    hight_pixels: int = 0,
    width_pixels: int = 0,
):
    jpg_list = list(path_pdf.glob("**/*.pdf"))

    img = Image.open(io.BytesIO(bytes_image))
    w, h = img.size

    w_crop_iterations = int(w / 1280)
    h_crop_iterations = int(h / 1280)
    for h_multiplication, h_iteration in enumerate(range(h_crop_iterations), 1):
        for w_multiplication, w_iteration in enumerate(range(w_crop_iterations), 1):
            crop_area = to_1280_format(h_multiplication, w_multiplication)

            # Print multiplication and crop area to check results
            print(
                "h mult {} w mult {}".format(h_multiplication - 1, w_multiplication - 1)
            )
            print(crop_area)

            # Crop image
            img_crop = img.crop(crop_area)

            # Resize to 1280x1280 format
            img_crop.thumbnail((width_pixels, hight_pixels))
            crop_save = path_convert_pdf / "{}_{}_{}.jpg".format(
                jpg_list[0].stem, h_multiplication - 1, w_multiplication - 1
            )
            img_crop.save(crop_save)


# Upload pdf and change to jpg
path_pdf = Path("wall_detection_export/upload_pdf")
path_convert_pdf = Path("wall_detection_export/convert_pdf")
path_export_txt = Path("wall_detection_export/export_txt")
path_model = Path("train_results/model_12classes/weights/best.pt")

converter = Convert_pdf(path_pdf=(path_pdf))
convert_file = converter.save_image(path_convert_pdf)

# Set detection model
detection_model = AutoDetectionModel.from_pretrained(
    model_type="yolov5_custom",
    model_path=path_model,
    confidence_threshold=0.3,
    device="cuda",  # or 'cuda:0'
)

# Slice prediction with sahi
result = get_sliced_prediction(
    str(convert_file),
    detection_model,
    slice_height=1280,
    slice_width=1280,
    overlap_height_ratio=0.2,
    overlap_width_ratio=0.2,
)
df_predictions = pd.DataFrame(
    columns=["number", "xmin", "ymin", "xmax", "ymax", "confidence", "class", "name"]
)
# print(result.to_coco_annotations())
print(result.object_prediction_list)
for n, dict in enumerate(result.to_coco_annotations()):
    print(dict.items())
    new_row = {"number":n, "xmin":dict["bbox"][0], "ymin":-(dict["bbox"][1]), "xmax":dict["bbox"][0]+dict["bbox"][2], "ymax":-(dict["bbox"][1]+dict["bbox"][3]), "confidence" :dict["score"], "class":dict["category_id"], "name":dict["category_name"]}
    df_predictions = pd.concat([df_predictions, pd.DataFrame([new_row])], ignore_index=True)
    # df_predictions = pd.append(new_row, ignore_index=True)
    # print(i["bbox"])
    # df = pd.DataFrame(i)
    # df_predictions = pd.concat([df_predictions, df])
df_predictions = df_predictions[df_predictions["name"] == "wall"]
df_predictions.to_csv(path_export_txt / "prediction_sahi.csv")
