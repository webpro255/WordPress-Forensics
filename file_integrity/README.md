# File Integrity Checking

This feature compares the core files of a WordPress installation with a clean version from WordPress.org to identify unauthorized changes or modifications. It checks file integrity by hashing each file and comparing the hashes to detect tampering or malware.

## Usage

1. Ensure you have Python installed on your machine.
2. Navigate to this folder in your terminal:
   ```bash
   cd file_integrity
   ```
3. Run the integrity check:
   ```
   python3 wp_file_integrity.py
   ```
## Dependencies
- Python 3.x
- `requests` library for downloading WordPress core files:
  ```
  pip3 install requests
  ```
## Future Plans
- Add support for custom WordPress installations with plugins and themes.
- Include a web-based interface for easier use.
