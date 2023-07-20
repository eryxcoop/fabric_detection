#FROM gcr.io/deeplearning-platform-release/pytorch-gpu
FROM us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13.py310:latest


ENV BUCKET_ROOT = "/gcs/covers_image_dataset/"
#ENV BUCKET_ROOT="/"

WORKDIR /

RUN pip install ultralytics
RUN pip install opencv-python
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY covers_prototype_train.py /covers_prototype_train.py

ENTRYPOINT ["python", "covers_prototype_train.py"]

#us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/flower_image:latest
#us-central1-docker.pkg.dev/computervision-392819/covers-image-train/covers-image-dataset:latest
