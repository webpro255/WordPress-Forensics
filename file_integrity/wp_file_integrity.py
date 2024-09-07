```python
import os
import hashlib
import requests
import zipfile

# Function to calculate the hash of a file
def calculate_file_hash(filepath, hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Function to download and extract WordPress core files
def download_wordpress(version="latest"):
    url = f"https://wordpress.org/{version}.zip"
    response = requests.get(url)
    zip_filename = f"{version}.zip"

    with open(zip_filename, 'wb') as file:
        file.write(response.content)

    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(f"./{version}")

# Function to compare file hashes between live and clean WordPress
def compare_wordpress_files(live_dir, clean_dir, hash_algo='sha256'):
    differences = []

    for root, _, files in os.walk(live_dir):
        for file in files:
            live_file_path = os.path.join(root, file)
            clean_file_path = live_file_path.replace(live_dir, clean_dir)

            if os.path.exists(clean_file_path):
                live_hash = calculate_file_hash(live_file_path, hash_algo)
                clean_hash = calculate_file_hash(clean_file_path, hash_algo)

                if live_hash != clean_hash:
                    differences.append(f"Modified: {live_file_path}")
            else:
                differences.append(f"New/Unknown file: {live_file_path}")

    return differences

# Main function
def main():
    # Download official WordPress core files (can specify version if needed)
    download_wordpress()

    # Compare the live WordPress files with the clean ones
    live_wordpress_path = "/var/www/html/wordpress"  # Example path to your live WordPress
    clean_wordpress_path = "./latest"  # Path to downloaded WordPress

    differences = compare_wordpress_files(live_wordpress_path, clean_wordpress_path)

    if differences:
        print("Potential integrity issues detected:")
        for diff in differences:
            print(diff)
    else:
        print("No integrity issues detected.")

if __name__ == "__main__":
    main()
