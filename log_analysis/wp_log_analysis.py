```python
import os
import re

# Function to parse WordPress debug log
def parse_wordpress_log(log_file):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found.")
        return

    with open(log_file, 'r') as file:
        logs = file.readlines()

    suspicious_activities = []
    for line in logs:
        if "error" in line.lower() or "warning" in line.lower():
            suspicious_activities.append(line.strip())

    if suspicious_activities:
        print("Suspicious activities found in WordPress log:")
        for activity in suspicious_activities:
            print(activity)
    else:
        print("No suspicious activities detected in WordPress log.")

# Function to parse Apache or Nginx access log
def parse_server_access_log(log_file):
    if not os.path.exists(log_file):
        print(f"Log file {log_file} not found.")
        return

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
    
    if frequent_ips:
        print("Potential brute force IPs found:")
        for ip, count in frequent_ips.items():
            print(f"IP: {ip}, Requests: {count}")
    else:
        print("No suspicious IPs detected in server access log.")

# Main function to run both log analyses
def main():
    wordpress_log = "/path/to/your/wp-content/debug.log"  # Replace with the actual path to your WordPress debug log
    server_log = "/path/to/your/server/access.log"  # Replace with the actual path to your server's access log

    print("Analyzing WordPress log...")
    parse_wordpress_log(wordpress_log)

    print("\nAnalyzing server access log...")
    parse_server_access_log(server_log)

if __name__ == "__main__":
    main()
