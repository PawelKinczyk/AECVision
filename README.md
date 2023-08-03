
# AECVision

AECVision is an object detection project for the construction industry. The main goal is to deliver good models for various problems like:
- Detection elements on plans to allow automatized tasks
- Speed up documentation analysis
- Create tools for future computer vision projects 

## Information

Now project is base on [YOLOv5](https://github.com/ultralytics/yolov5) repo but in the future I will try other types of model architectures.

- Input image resolution 1280x1280
- Image file .jpg
- For tagging i use [Label Studio](https://labelstud.io/)
- Training model in [Google Colab](https://colab.google/)
- Detection images with using [Sahi](https://github.com/obss/sahi)

### Folder structure
```
virtual-env # Here you should have your virtual-env
modules # Project modules
├───object_detection # Detection screen module
│   └───screen_detection.ipynb 
├───prepare_data_and_training # Prepare data and training in google colab module
│   ├───dataset
│   │   ├───images
│   │   │   ├───test
│   │   │   ├───training
│   │   │   └───validation
│   │   └───labels
│   │       ├───labels_reduce_classes
│   │       ├───test
│   │       ├───training
│   │       └───validation
│   ├───prepare_data_from_pdf.ipynb
│   └───train_model_in_google_colab.ipynb
├───wall_detection_export # Export walls detection coordinates to csv and allow imports in other program
│   ├───files
│   │   ├───converted_pdf
│   │   ├───exported_csv
│   │   └───upload_pdf
│   ├───classes_functions.py
│   ├───wall_detection_export_with_sahi.py
│   └───wall_detection_export.py
train_results # Available modules
├───model_12classes
├───model_12classes_gray
├───model_walls
└───model_walls_gray
yolov5 # Cloned Yolov5 repository
LICENSE
README.md
requirements.txt
```

### Project pipeline
![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/3a8048ff-2d91-4bd8-bc95-834dd4cc1ec7)

### Available models

| Name | Classes | Model architecture | Number of training images [original/augmented] | Color |
|------|---------|--------------------|------------------------------------------------|-------|
| model_12classes | 12 Classes (see train_results) |  YOLOv5m6 | 252 / 1204 | RGB |
| model_walls | Wall |  YOLOv5m6 | 252 / 1204 | RGB |
| model_12classes_gray | 12 Classes (see train_results) |  YOLOv5m6 | 252 / 1204 | GRAY |
| model_walls_gray | Wall |  YOLOv5m6 | 252 / 1204 | GRAY |

[![MIT License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/PawelKinczyk/AECVision/blob/main/LICENSE) 

## How it works?

The model was trained on clear plans and with annotation but remember that the best results you get without many symbols on construction plans. 

### Detection
#### Confidence = 0.5
![Za -5-Projekt-architektoniczno-budowlany pdf2_2_3](https://github.com/PawelKinczyk/AECVision/assets/96824698/f26e7b79-2da5-42d9-8490-d8eed6da295e)

#### Confidence = 0.8
![Za -5-Projekt-architektoniczno-budowlany pdf2_2_31](https://github.com/PawelKinczyk/AECVision/assets/96824698/3a28a1b9-8124-434c-8af8-8033a32b8e68)

### Screen detection
By using screen_detection.py

https://github.com/PawelKinczyk/AECVision/assets/96824698/0e60f9e4-a5dd-4fdc-a695-ea3c943e4a7f

## Project roadmap

- [ ]  Collect and tag more images (up to 500)
- [ ]  Try to use Grayscale than RGB
- [ ]  Change number of classes (maybe only 3? Wall, Window, Door)
- [ ]  Evolve hyperparameters to get the best set (in YOLO)
- [ ]  Use other model architecture (than YOLO)
- [ ]  Think about switch from .jpg file to .png (avoid converting data lost)
- [ ]  Think about how to add more "contexts" to the model (like: you are in the kitchen if there are stove and there probably will be table)


## Summary & Problems

### First training
#### Data description
Walls are overrepresented because this is normal quantities in architectural plans.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/97386b7d-19fe-4136-962a-5b99707d823d)

Maybe in future, i need to create more plans with other categories to improve other classes detection.

#### Learning process
##### Model has steadily improved up to the 272nd epoch and probably has further potential.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/abc451d1-2ea0-497d-bbf7-9b5a6ca45d62)

##### On the validation set, an increase in "obj_loss" was noted during the learning process.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/f1217a7b-fc9f-4d62-a7b3-862025eedf28)

##### Confussion matrix show that all classes except "background" are correctly identified.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/f4c0b780-fff5-4bf7-a138-2e4333206a8f)

##### If you want to dig into training results see train_results or write to me.

#### Problems
- A small number of certain classes
- Conversion from pdf (default construction plans format) to jpg results in a loss of image quality

## Contributing

Contributions are always welcome! I look for help in tagging and improving models. Feel free to improve this project.


## Thanks

Thanks, [YOLOv5](https://github.com/ultralytics/yolov5) and [Label Studio](https://labelstud.io/) for your project and tutorials.
Special thanks to my brother Marcin who help me with tagging.

<a href="https://www.buymeacoffee.com/produktywnl" target="blank"><img align="center" src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" title = "Buy me coffee" alt="" height="50" /></a>
