from pathlib import Path
import cv2
import torch
from mss import mss
import numpy as np
from PIL import Image


models_list = [Path("train_results/model_12classes/weights/best.pt"),
               Path("train_results/model_12classes_gray/weights/best.pt"),
               Path("train_results/model_walls/weights/best.pt"),
               Path("train_results/model_walls_gray/weights/best.pt")
               ]

# Pick model number and detection confidence
pick_model = 1
detection_confidence = 0.6

model = torch.hub.load(
    "yolov5", 'custom', path=models_list[pick_model], source='local', force_reload=True)
model.conf = detection_confidence
sct = mss()


while True:
    w, h = 1920, 1080
    monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}
    if pick_model == 0 or pick_model == 3:
        img = Image.frombytes('RGB', (w, h), sct.grab(monitor).rgb)
        screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        img = Image.frombytes('RGB', (w, h), sct.grab(monitor).rgb)
        screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    # Get result of model
    result = model(screen, size=1280)

    cv2.imshow('Screen', result.render()[0])

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
