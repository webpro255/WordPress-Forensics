# Log Analysis for WordPress

This feature analyzes WordPress logs (e.g., `wp-content/debug.log`) and server access logs (Apache or Nginx) to detect suspicious activities such as unauthorized logins, file modifications, or brute-force attacks.

## Features of the Log Analysis Script:

    WordPress Log Parsing: It checks for "error" or "warning" keywords in the WordPress debug log to flag issues.
    Server Access Log Parsing: It scans the access logs for frequent IPs (indicating brute force attacks or suspicious behavior).

## Usage

1. Ensure you have Python installed.
2. Navigate to this folder in your terminal:
   ```bash
   cd log_analysis
   ```
3. Run the log analysis script:
   ```
   python3 wp_log_analysis.py
   ```
4.  Replace the paths "`/path/to/your/wp-content/debug.log`" and "`/path/to/your/server/access.log`" with the actual paths to your logs.


## What the Script Does:

### WordPress Log Analysis:
- Parses the WordPress debug.log and looks for suspicious patterns such as errors, warnings, failed logins, or possible SQL injection attempts.
- Logs are printed to the console with timestamps when suspicious activities are found.

### Server Access Log Analysis:
- Analyzes the server's access log (Apache or Nginx) for frequent IP addresses. IPs with over 10 requests are flagged as potential brute-force attempts.
- The flagged IPs are printed to the console for review.
   
 
## Future Plans
- Integrate with email alerts to notify admins of suspicious activity.
