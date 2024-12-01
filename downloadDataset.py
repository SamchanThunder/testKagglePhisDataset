from kaggle.api.kaggle_api_extended import KaggleApi
import os

#Token
os.environ["KAGGLE_CONFIG_DIR"] = "~/.kaggle/kaggle.json"

api = KaggleApi()
api.authenticate()

#Download
dataset = "subhajournal/phishingemails"
download_path = "./phishingemails_dataset"
os.makedirs(download_path, exist_ok=True)
api.dataset_download_files(dataset, path=download_path, unzip=True)

print(f"Dataset downloaded to: {download_path}")
