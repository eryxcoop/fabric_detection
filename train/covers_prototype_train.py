from ultralytics import YOLO
import shutil
#BUCKET_ROOT = "/gcs/covers_image_dataset"


model = YOLO("yolov8n-cls.pt")

dataset_path = "images"

number_of_epochs = 1

model.train(data=dataset_path, epochs=number_of_epochs)


source = "runs"
destination = "/gcs/covers_image_dataset"
shutil.move(source, destination)
