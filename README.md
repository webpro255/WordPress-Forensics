# WordPress Forensics Tool

A forensics tool designed to analyze WordPress installations, check file integrity, review logs, and detect malware.

## Features
- File integrity checks for WordPress core files.
- Log analysis for suspicious user activity.
- Web server access log analysis.
- Database activity tracking.

## Installation
Clone the repository and run the script:
```bash
git clone https://github.com/webpro255/WordPress-Forensics.git
cd WordPress-Forensics
```
## Usage
Run the tool using:
```
python3 wp_forensics.py
```
## Customize for Your Environment
- Change the path to your actual live WordPress installation (e.g., `/var/www/html/wordpress`).
- You can specify a version of WordPress by replacing "`latest`" with the version number (e.g., "`5.8.1`").

1. Navigate to the directory where you saved the script.
2. Run the script:
```
python3 wp_file_integrity.py
```
## Check for Results
The script will compare your live WordPress installation against the clean files and list any files that have been modified or are unknown


