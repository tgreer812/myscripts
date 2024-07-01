import os
import zipfile
import requests

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"Downloaded {url} to {dest_path}")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

def main():
    url = 'https://download.sysinternals.com/files/SysinternalsSuite.zip'
    zip_file_path = 'SysinternalsSuite.zip'
    extract_to_folder = 'sysinternals'

    # Download the Sysinternals Suite
    download_file(url, zip_file_path)

    # Create the target directory if it doesn't exist
    if not os.path.exists(extract_to_folder):
        os.makedirs(extract_to_folder)

    # Extract the zip file into the target directory
    extract_zip(zip_file_path, extract_to_folder)

    # Clean up the zip file
    os.remove(zip_file_path)
    print(f"Removed {zip_file_path}")

if __name__ == "__main__":
    main()
