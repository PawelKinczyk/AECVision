
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
insert pipeline image

### Availabe models

| Name | Classes | Model architecture | Number of training images [original/augmented] |
|------|---------|--------------------|------------------|
| traine_best | 12 Classes (see train_results/traine_best/labels.jpg) |  YOLOv5m6 | 252 / 1204 |


![master](https://img.shields.io/github/last-commit/badges/shields/master)
[![MIT License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/PawelKinczyk/AECVision/blob/main/LICENSE) 



## How it works?

The model was trained on clear plans and with annotation but remember that the best results you get without many symbols on construction plans. 

### Detection

images

### Screen detection


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


## Contributing

Contributions are always welcome! I look for help in tagging and improving models. Feel free to improve this project.


## Thanks

Thanks, [YOLOv5](https://github.com/ultralytics/yolov5) and [Label Studio](https://labelstud.io/) for your project and tutorials.
Special thanks to my brother Marcin who help me with tagging.

