import os
import re
from datetime import datetime

# Customizable suspicious patterns (keywords to detect)
SUSPICIOUS_PATTERNS = ['error', 'warning', 'login failed', 'SQL', 'injection', 'file modification']

# Function to parse WordPress debug log
def parse_wordpress_log(log_file):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found.")
        return []

    with open(log_file, 'r') as file:
        logs = file.readlines()

    suspicious_activities = []
    for line in logs:
        if any(pattern.lower() in line.lower() for pattern in SUSPICIOUS_PATTERNS):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            suspicious_activities.append(f"[{timestamp}] {line.strip()}")

    return suspicious_activities

# Function to parse Apache or Nginx access log
def parse_server_access_log(log_file):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found.")
        return []

    suspicious_ips = {}
    with open(log_file, 'r') as file:
        for line in file:
            ip = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
            if ip:
                ip = ip[0]
                if suspicious_ips.get(ip):
                    suspicious_ips[ip] += 1
                else:
                    suspicious_ips[ip] = 1

    # Flag IPs that appear frequently (potential brute-force attempts)
    frequent_ips = {ip: count for ip, count in suspicious_ips.items() if count > 10}
    
    return frequent_ips

# Main function to run log analysis
def main():
    wordpress_log = "/path/to/your/wp-content/debug.log"  # Replace with actual path
    server_log = "/path/to/your/server/access.log"  # Replace with actual path

    # Analyze WordPress log
    print("Analyzing WordPress log...")
    wp_suspicious = parse_wordpress_log(wordpress_log)
    if wp_suspicious:
        print("Suspicious activities found in WordPress log:")
        for activity in wp_suspicious:
            print(activity)
    else:
        print("No suspicious activities detected in WordPress log.")

    # Analyze server access log
    print("\nAnalyzing server access log...")
    server_suspicious = parse_server_access_log(server_log)
    if server_suspicious:
        print("Potential brute force IPs found:")
        for ip, count in server_suspicious.items():
            print(f"IP: {ip}, Requests: {count}")
    else:
        print("No suspicious IPs detected in server access log.")

if __name__ == "__main__":
    main()
