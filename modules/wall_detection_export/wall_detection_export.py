from pathlib import Path
from PIL import Image
import torch
import pandas as pd
import shutil
import os

from classes_functions import Convert_pdf, crop_image


# Upload pdf and change to jpg
path_upload_pdf = Path("modules/wall_detection_export/files/upload_pdf")
path_convert_pdf = Path("modules/wall_detection_export/files/converted_pdf")
path_export_txt = Path("modules/wall_detection_export/files/exported_csv")
path_model = Path("train_results/model_12classes/weights/best.pt")

# Convert pdf to jpg
converter = Convert_pdf(path_pdf=path_upload_pdf)
data = converter.return_pixmap()

# Crop image to 1280x1280
crop_image(
    path_pdf=path_upload_pdf,
    path_convert_pdf=path_convert_pdf,
    hight_pixels=1280,
    width_pixels=1280,
    bytes_image=data,
)

# Setup model
model = torch.hub.load("yolov5", "custom", path=path_model, source="local")
model.conf = 0.8  # Define model confidence

# Pandas dataframe to store predictions
df_predictions = pd.DataFrame()

for file in path_convert_pdf.glob("**/*.jpg"):
    # Open file image and get image row and column
    file_name = file.stem.split("_")
    img = Image.open(file)

    # Model prediction
    results = model(img, size=1280)
    predictions = results.pandas().xyxy[0]
    df = pd.DataFrame(predictions)
    # Save only walls detection
    # I multiply them by 1280 to account image location in full pdf
    df = df[df["name"] == "wall"]
    df["ymin"] = -(df["ymin"] + float(file_name[1]) * 1280)
    df["ymax"] = -(df["ymax"] + float(file_name[1]) * 1280)
    df["xmin"] = df["xmin"] + float(file_name[2]) * 1280
    df["xmax"] = df["xmax"] + float(file_name[2]) * 1280

    # Add image prediction to all predictions
    df_predictions = pd.concat([df_predictions, df])
    image_prediction = path_export_txt / "image"

    # Save image with predictions
    # This proces is needed because prediction are save in subfolder...
    results.save(save_dir=image_prediction)
    for filename in os.listdir(image_prediction):
        source_file_path = os.path.join(image_prediction, filename)
        destination_file_path = os.path.join(path_export_txt, filename)
        shutil.move(source_file_path, destination_file_path)
    shutil.rmtree(image_prediction)

# Save predictions to csv in export_txt folder
df_predictions.to_csv(path_export_txt / "prediction.csv")
