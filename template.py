import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'lung_cancer_project'

# List of folders and files based on your structure
list_of_folders = [
    f"{project_name}/static/uploads",      # Folder for uploaded images
    f"{project_name}/templates",           # Folder for HTML files
    f"{project_name}/model",               # Folder for models
    f"{project_name}/database",            # Folder for the SQLite database
]

list_of_files = [
    f"{project_name}/templates/index.html",         # HTML file for frontend
    f"{project_name}/model/lung_model.h5",         # Trained CNN model file
    f"{project_name}/database/lung_cancer.db",     # SQLite database file
    f"{project_name}/app.py",                      # Main Flask app file
    f"{project_name}/train_model.py",              # Script to train the model
    f"{project_name}/requirements.txt",            # Python libraries required for the project
    f"{project_name}/README.md",                   # Project documentation
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
                f.write("# Lung Cancer Detection Project\n")  # Initial README content
            elif filename.endswith(".py"):
                f.write("# Python file\n")  # Initial Python file content
            elif filename.endswith(".html"):
                f.write("<!-- HTML template -->\n")  # Initial HTML file content
            elif filename.endswith(".txt"):
                f.write("# requirements\n")  # Initial requirements content
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
