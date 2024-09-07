# Log Analysis for WordPress

This feature analyzes WordPress logs (e.g., `wp-content/debug.log`) and server access logs (Apache or Nginx) to detect suspicious activities such as unauthorized logins, file modifications, or brute-force attacks.

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
## Future Plans

- Add detection for specific attack patterns (e.g., brute force login attempts).
- Integrate with email alerts to notify admins of suspicious activity.
