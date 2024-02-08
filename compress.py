import os
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compression_type):
    try:
        folder_name = os.path.basename(folder_path)
        current_date = datetime.now().strftime("%Y_%m_%d")
        compressed_file_name = f"{folder_name}_{current_date}.{compression_type}"

        if compression_type == "tgz":
            with tarfile.open(compressed_file_name, "w:gz") as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compression_type == "zip":
            with zipfile.ZipFile(compressed_file_name, "w") as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)

        print(f"Compression successful! File saved as: {compressed_file_name}")

    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compression_types = ["tgz", "zip"]

    print("Available compression types:")
    for idx, comp_type in enumerate(compression_types, start=1):
        print(f"{idx}. {comp_type}")

    try:
        selection = int(input("Select the desired compression type (enter the number): "))
        if selection < 1 or selection > len(compression_types):
            raise ValueError("Invalid selection")

        selected_compression_type = compression_types[selection - 1]

        compress_folder(folder_path, selected_compression_type)

    except ValueError as ve:
        print(f"Invalid input. {str(ve)}")

if __name__ == "__main__":
    main()
