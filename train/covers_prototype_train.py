from ultralytics import YOLO
from datetime import datetime
import shutil
import torch
import os

BUCKET_ROOT = os.environ["BUCKET_ROOT"]
print("La variable de entorno es:"+ BUCKET_ROOT)

if torch.cuda.is_available():
    print("Cuda is available :)")

model = YOLO("yolov8n-cls.pt")

dataset_path = BUCKET_ROOT + "/" + "images"

number_of_epochs = 1

model.train(data=dataset_path, epochs=number_of_epochs)

source = "runs"

date_timestamp = datetime.now().strftime("%d%m%Y_%H%M")
destination = "/gcs/covers_image_dataset/results/" + date_timestamp
shutil.move(source, destination)
