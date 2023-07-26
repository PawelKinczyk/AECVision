from pathlib import Path
import pandas as pd
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

from classes_functions import Convert_pdf

# Upload pdf and change to jpg
path_upload_pdf = Path("wall_detection_export/upload_pdf")
path_convert_pdf = Path("wall_detection_export/convert_pdf")
path_export_txt = Path("wall_detection_export/export_txt")
path_model = Path("train_results/model_12classes/weights/best.pt")

# Convert pdf to jpg
converter = Convert_pdf(path_pdf=path_upload_pdf)
convert_file = converter.save_image(path_convert_pdf)

# Setup model
detection_model = AutoDetectionModel.from_pretrained(
    model_type="yolov5_custom",
    model_path=path_model,
    confidence_threshold=0.3,  # Define model confidence
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

# Pandas dataframe to store predictions
df_predictions = pd.DataFrame(
    columns=["number", "xmin", "ymin", "xmax", "ymax", "confidence", "class", "name"]
)

for n, dict in enumerate(result.to_coco_annotations()):

    # Add all predictions to df_predictions data frame
    new_row = {
        "number": n,
        "xmin": dict["bbox"][0],
        "ymin": -(dict["bbox"][1]),
        "xmax": dict["bbox"][0] + dict["bbox"][2],
        "ymax": -(dict["bbox"][1] + dict["bbox"][3]),
        "confidence": dict["score"],
        "class": dict["category_id"],
        "name": dict["category_name"],
    }
    df_predictions = pd.concat(
        [df_predictions, pd.DataFrame([new_row])], ignore_index=True
    )

# Save only walls detection
df_predictions = df_predictions[df_predictions["name"] == "wall"]

# Save predictions to csv in export_txt folder
df_predictions.to_csv(path_export_txt / "prediction_sahi.csv")

# Save image with recognitions
result.export_visuals(export_dir=path_export_txt, text_size=1.0, rect_th=1)
