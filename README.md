# Process-Monitor
Periodic Process Logger with Auto Scheduled Log Report Facility.

This automation script is written in pyhton 3.

This scripts stores the process running in the machine with their PID, name and username in log file and mails the file from the provided sender's mail-id to receiver's mail-id.
It can be scheduled to run after a certain time interval provided by the user (should be provided in terms of minutes).

To run the script:
python3 main.py [OPTIONS] or [PATH]
 
OPTIONS:   -h help
           -u usage
  
PATH:       Absolute path where you want to create the log file.
