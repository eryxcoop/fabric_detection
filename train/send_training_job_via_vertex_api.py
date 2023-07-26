#my_job = aiplatform.CustomContainerTrainingJob(display_name='flower-sdk-job',
#                                               container_uri='us-central1-docker.pkg.dev/{PROJECT_ID}/flower-app/flower_image:latest',
#                                               staging_bucket='gs://{BUCKET}')

from google.cloud import aiplatform

my_job = aiplatform.CustomContainerTrainingJob(display_name='covers-prototype-aivertexsdk-test',
                                               container_uri='us-central1-docker.pkg.dev/computervision-392819/covers-image-train/covers-image-dataset:latest',
                                               staging_bucket='gs://covers_image_dataset')

my_job.run(replica_count=1,machine_type='n1-standard-8')

#           accelerator_type='NVIDIA_TESLA_V100',
#           accelerator_count=1)
