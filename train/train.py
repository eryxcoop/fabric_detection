
BUCKET_ROOT = "/gcs/covers_image_dataset"

file_name = 'readme.txt'

file_path = f"{BUCKET_ROOT}/{file_name}"


with open(file_path, 'r') as file:
    first_line = file.readline()



with open(f"{BUCKET_ROOT}/segundo_archivo.txt", 'w') as f:
    f.write("la lectura fue exitosa y leimos:\n")
    f.write(first_line)

# from google.cloud import storage
# storage_client = storage.Client.from_service_account_json("credentials.json")
# bucket = storage_client.get_bucket("eryx-toyota-bucket")
# # blob = bucket.get_blob("fotos-290323/2023-03-29-114718.jpg")
# # blob.download_to_filename("fotito_del_blob.jpg")

# blob = bucket.blob(file_name)
# blob.upload_from_filename(file_name)

# # esto podría levantar el bucket y llamar al train.py con los parámetros que le seteamos en este archivo

