from ultralytics import YOLO
import random
import cv2
import numpy as np

model = YOLO('my_model_segmen_full_integer_quant_edgetpu.tflite', task='segment') 

img = cv2.imread("1xa.png")
#img1 = cv2.imread("1a.jpg")
img1 = np.ones(img.shape, dtype=np.uint8)
img1.fill(255)
# if you want all classes
yolo_classes = list(model.names.values())
classes_ids = [yolo_classes.index(clas) for clas in yolo_classes]

conf = 0.2

results = model.predict(img, conf=conf)
colors = [random.choices(range(256), k=3) for _ in classes_ids]

isClosed = True
color = (255,0,0)
thickness = 2

for result in results:
    for mask, box in zip(result.masks.xy, result.boxes):
        points = np.int32([mask])
        color_number = classes_ids.index(int(box.cls[0]))
        #cv2.fillPoly(img, points, colors[color_number])
        cv2.fillPoly(img1, points, 0)
        #cv2.polylines(img1, points, isClosed, color, thickness)
        

masked_image = cv2.bitwise_or(img, img1)
cv2.imshow("Image", masked_image)
cv2.waitKey(0)

cv2.imwrite("test.jpg", img)
# https://flows.nodered.org/node/@roaders/node-red-contrib-image-path-crop
