from ultralytics import YOLO

BUCKET_ROOT = "/gcs/covers_image_dataset"

model = YOLO("yolov8n-cls.pt")

dataset_path = BUCKET_ROOT + "/images"

model.train(data=dataset_path, epochs=100)