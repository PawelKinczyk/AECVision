import cv2
import torch
from mss import mss
import numpy as np
from PIL import Image


model = torch.hub.load("yolov5", 'custom', path="train_results/traine_best/weights/best.pt", source='local')
model.conf = 0.6 # Define model confidence
sct = mss()


while 1:
    w, h = 1920, 1080
    monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}
    img = Image.frombytes('RGB', (w, h), sct.grab(monitor).rgb)
    screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Get result of model
    result = model(screen, size=1280)

    cv2.imshow('Screen', result.render()[0])

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

