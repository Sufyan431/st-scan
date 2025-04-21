# Lung Cancer Detection using CT-Scan Images 🫁

This is an end-to-end deep learning project using CNN with Flask, HTML, and SQLite. It classifies lung CT-scan images as `benign`, `malignant`, or `normal`.

## 🗂️ Project Structure

<!--
lung_cancer_project/
│
├── static/
│   └── uploads/                ← Folder for uploaded CT scan images
│
├── templates/
│   └── index.html              ← Main frontend for upload & result display
│
├── model/
│   └── lung_model.h5           ← Trained CNN model (VGG19 + ResNet101)
│
├── notebook/
│   └── train_test_model.ipynb  ← Jupyter Notebook — model training, testing, and visualization
│
├── database/
│   └── lung_cancer.db          ← SQLite database for storing predictions
│
├── dataset/
│   └── prepare_dataset.py      ← Script to download & extract dataset
│
├── app.py                      ← Main Flask app
├── train_model.py              ← Script for training CNN model
├── requirements.txt            ← Python dependencies
└── README.md                   ← Project documentation
-->

