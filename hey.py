import os
import shutil

# Directorio de imágenes de entrada
input_dir = input("ingresa dir: ")

# Directorios de salida para máscaras y no máscaras
output_mask_dir = "mask"
output_no_mask_dir = "image"

# Crea los directorios de salida si no existen
os.makedirs(output_mask_dir, exist_ok=True)
os.makedirs(output_no_mask_dir, exist_ok=True)

# Recorre el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith("_mask.png"):
        # Si el nombre de archivo termina en "_mask.png", es una máscara
        src_path = os.path.join(input_dir, filename)
        dest_path = os.path.join(output_mask_dir, filename)
        shutil.move(src_path, dest_path)
    elif filename.endswith(".jpg"):
        # Si el nombre de archivo termina en ".jpg", no es una máscara
        src_path = os.path.join(input_dir, filename)
        dest_path = os.path.join(output_no_mask_dir, filename)
        shutil.move(src_path, dest_path)

print("Separación de imágenes completa.")
