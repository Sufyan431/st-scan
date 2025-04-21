import gdown
import zipfile
import os

# Google Drive shared file link
file_id = "1hopFjmqJu0dG1S0D0KqHPjAXhluB7ICf"
output_zip = "lung_dataset.zip"

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", output_zip, quiet=False)

# Extract the zip file
with zipfile.ZipFile(output_zip, 'r') as zip_ref:
    zip_ref.extractall("data")  # Extract into a 'data/' folder

# Remove the zip after extraction (optional)
os.remove(output_zip)

print("✅ Dataset downloaded and extracted successfully.")
