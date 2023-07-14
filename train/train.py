file_name = 'readme.txt'

with open(file_name, 'w') as f:
    f.write('Create a new text file!')

from google.cloud import storage
storage_client = storage.Client.from_service_account_json("credentials.json")
bucket = storage_client.get_bucket("eryx-toyota-bucket")
# blob = bucket.get_blob("fotos-290323/2023-03-29-114718.jpg")
# blob.download_to_filename("fotito_del_blob.jpg")

blob = bucket.blob(file_name)
blob.upload_from_filename(file_name)

# esto podría levantar el bucket y llamar al train.py con los parámetros que le seteamos en este archivo