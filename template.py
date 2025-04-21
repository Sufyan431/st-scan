import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'lung_cancer_project'

# List of folders (including dataset folder now)
list_of_folders = [
    f"{project_name}/static/uploads",      # For uploaded images
    f"{project_name}/templates",           # HTML templates
    f"{project_name}/model",               # Trained model
    f"{project_name}/database",            # SQLite DB
    f"{project_name}/dataset",             # 📁 Dataset folder added
]

# List of files (prepare_dataset.py included)
list_of_files = [
    f"{project_name}/templates/index.html",
    f"{project_name}/model/lung_model.h5",
    f"{project_name}/database/lung_cancer.db",
    f"{project_name}/dataset/prepare_dataset.py",   # ✅ New script to download & unzip dataset
    f"{project_name}/app.py",
    f"{project_name}/train_model.py",
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md",
]

# Create folders
for folder in list_of_folders:
    folder_path = Path(folder)
    if not folder_path.exists():
        os.makedirs(folder_path)
        logging.info(f"Created directory: {folder_path}")
    else:
        logging.info(f"Directory already exists: {folder_path}")

# Create files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if not filepath.exists():
        with open(filepath, 'w') as f:
            if filename == "README.md":
                f.write("# Lung Cancer Detection Project\n")
            elif filename == "prepare_dataset.py":
                f.write("# This script will download and extract dataset from Google Drive\n")
            elif filename.endswith(".py"):
                f.write("# Python file\n")
            elif filename.endswith(".html"):
                f.write("<!-- HTML template -->\n")
            elif filename.endswith(".txt"):
                f.write("# requirements\n")
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
    
    