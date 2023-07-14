FROM gcr.io/deeplearning-platform-release/pytorch-gpu

WORKDIR /

COPY train.py /train.py
COPY credentials.json /credentials.json

ENTRYPOINT ["python", "train.py"]
