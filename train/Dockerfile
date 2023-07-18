FROM gcr.io/deeplearning-platform-release/pytorch-gpu

WORKDIR /

COPY train.py /train.py
#COPY credentials.json /credentials.json

ENTRYPOINT ["python", "train.py"]

#us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/flower_image:latest
#us-central1-docker.pkg.dev/computervision-392819/covers-image-train/covers-image-dataset:latest
