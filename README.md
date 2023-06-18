
# AECVision

AECVision is an object detection project for the construction industry. The main goal is to deliver good models for various problems like:
- Detection elements on plans to allow automatized tasks
- Speed up documentation analysis
- Create tools for future new computer vision projects 

## Information

Now project is base on [YOLOv5](https://github.com/ultralytics/yolov5) repo but in the future I will try other types of model architectures.

- Input image resolution 1280x1280
- Image file .jpg
- For tagging i use [Label Studio](https://labelstud.io/)

### Project pipeline
![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/09d22837-d2b4-4b8d-adde-acbbb3dfffab)

### Available models

| Name | Classes | Model architecture | Number of training images [original/augmented] |
|------|---------|--------------------|------------------------------------------------|
| traine_best | 12 Classes (see train_results/traine_best/labels.jpg) |  YOLOv5m6 | 252 / 1204 |


![master](https://img.shields.io/github/last-commit/badges/shields/master)
[![MIT License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/PawelKinczyk/AECVision/blob/main/LICENSE) 



## How it works?

The model was trained on clear plans and with annotation but remember that the best results you get without many symbols on construction plans. 

### Detection
#### Confidence = 0.5
![Za -5-Projekt-architektoniczno-budowlany pdf2_2_3](https://github.com/PawelKinczyk/AECVision/assets/96824698/f7b43709-e9e5-4b16-9723-70306e202125)
#### Confidence = 0.8
![Za -5-Projekt-architektoniczno-budowlany pdf2_2_31](https://github.com/PawelKinczyk/AECVision/assets/96824698/de853059-628b-4474-831e-765c59835d64)


### Screen detection
By using screen_detection.py

https://github.com/PawelKinczyk/AECVision/assets/96824698/f311eab2-11e9-483b-9a99-11136c1eaf29


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

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/e515fdd1-bf00-40f6-9216-5d6eb6fd6c7f)

Maybe in future, i need to create more plans with other categories to improve other classes detection.

#### Learning process
##### Model has steadily improved up to the 272nd epoch and probably has further potential.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/83dbea04-a7cd-4380-ae17-2158114dec9a)

##### On the validation set, an increase in "obj_loss" was noted during the learning process.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/cdcf25ed-8ea4-4ab1-8f2e-d3655176fdf7)

##### Confussion matrix show that all classes except "background" are correctly identified.

![image](https://github.com/PawelKinczyk/AECVision/assets/96824698/0f917feb-e89d-4fe7-9df9-4eb1d18c59fb)

##### If you want to dig into training results see train_results or write to me.

#### Problems
- A small number of certain classes
- Conversion from pdf (default construction plans format) to jpg results in a loss of image quality

## Contributing

Contributions are always welcome! I look for help in tagging and improving models. Feel free to improve this project.


## Thanks

Thanks, [YOLOv5](https://github.com/ultralytics/yolov5) and [Label Studio](https://labelstud.io/) for your project and tutorials.
Special thanks to my brother Marcin who help me with tagging.

