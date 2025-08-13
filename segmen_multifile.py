from ultralytics import YOLO
import random
import cv2
import numpy as np
import pandas as pd
import glob
import os

model = YOLO('my_model_segmen_full_integer_quant_edgetpu.tflite', task='segment') 

#img = cv2.imread("2.png")
#img1 = cv2.imread("1a.jpg")
image_folder = '/home/pi/segmen/jpg'
output_folder = '/home/pi/segmen/result_jpg'
image_files = glob.glob(os.path.join(image_folder, '*.jpg')) + \
              glob.glob(os.path.join(image_folder, '*.png')) + \
              glob.glob(os.path.join(image_folder, '*.jpeg'))
# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# if you want all classes
yolo_classes = list(model.names.values())
classes_ids = [yolo_classes.index(clas) for clas in yolo_classes]

conf = 0.9

colors = [random.choices(range(256), k=3) for _ in classes_ids]

isClosed = True
color = (255,0,0)
thickness = 2

# Loop through each image and perform object detection
for image_path in image_files:
        # Read the image
    img = cv2.imread(image_path)
    img1 = np.ones(img.shape, dtype=np.uint8)
    img1.fill(255)
    if img is None:
        print(f"Could not read image: {image_path}")
        continue
        
        # Perform inference
    results = model.predict(img, conf=conf)
    for result in results:
            for mask, box in zip(result.masks.xy, result.boxes):
                    points = np.int32([mask])
                    color_number = classes_ids.index(int(box.cls[0]))
                    #cv2.fillPoly(img, points, colors[color_number])
                    cv2.fillPoly(img1, points, 0)
                    #cv2.polylines(img1, points, isClosed, color, thickness)
    masked_image = cv2.bitwise_or(img, img1)
    #cv2.imshow("Image", masked_image)
    output_filename = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_filename, masked_image)
    print(f"Processed and saved: {output_filename}")
print("Object Segmentation complete for all images in the folder.")
