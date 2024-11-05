from flask import Flask, jsonify
import kagglehub
import shutil
import os

app = Flask(__name__)

@app.route('/download_kaggle_dataset', methods=['GET'])
def download_kaggle_dataset():
    print('Start Downloading')
    # Download dataset using kagglehub
    path = kagglehub.dataset_download("mmontiel/tiny-lisa-traffic-sign-detection-dataset")
    print("Path to dataset files:", path)

    # Move dataset to Google Drive if needed, otherwise keep on server
    destination_directory = "/content"  # Change this to your desired location
    shutil.move(path, destination_directory)
    print('Done Downloading')
    return jsonify({"message": f"Dataset moved to {destination_directory}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
