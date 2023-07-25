BUCKET_ROOT = "/gcs/covers_image_dataset"

file_name = 'readme.txt'

file_path = f"{BUCKET_ROOT}/{file_name}"

with open(file_path, 'r') as file:
    first_line = file.readline()

with open(f"{BUCKET_ROOT}/segundo_archivo.txt", 'w') as f:
    f.write("la lectura fue exitosa y leimos:\n")
    f.write(first_line)
