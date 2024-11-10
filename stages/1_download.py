import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Set download directory
local_path = os.getcwd()
download_path = os.path.join(local_path, "download")
os.makedirs(download_path, exist_ok=True)

# Base URL
base_url = "https://files.docking.org/2D/"

# Fetch directory list
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
directories = [link.get("href").strip("/") for link in soup.find_all("a") if link.get("href") and len(link.get("href").strip("/")) == 2]

# Prepare file list and download
total_files = 0
file_urls = []

# Collect all files to download
for directory in directories:
    dir_url = f"{base_url}{directory}/"
    response = requests.get(dir_url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    files = [link.get("href") for link in soup.find_all("a") if link.get("href") and link.get("href").endswith(".txt")]
    total_files += len(files)
    for file in files:
        file_url = f"{dir_url}{file}"
        file_path = os.path.join(download_path, directory, file)
        file_urls.append((file_url, file_path))

# Download all files with progress bar
for file_url, file_path in tqdm(file_urls, total=total_files, desc="Downloading files"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(file_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

print("Download completed.")
