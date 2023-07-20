from ultralytics import YOLO
from datetime import datetime
import shutil
import torch
BUCKET_ROOT = "/gcs/covers_image_dataset"

if torch.cuda.is_available():
    print("Cuda is available :)")

model = YOLO("yolov8n-cls.pt")

dataset_path = BUCKET_ROOT + "/"+"images"

number_of_epochs = 100

model.train(data=dataset_path, epochs=number_of_epochs)


source = "runs"

date_timestamp = datetime.now().strftime("%d%m%Y_%H%M")
destination = "/gcs/covers_image_dataset/results/" + date_timestamp
shutil.move(source, destination)
