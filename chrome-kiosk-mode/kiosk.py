import subprocess
import sys

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Update with the actual path to your Chrome executable
url = sys.argv[1]  # Get the URL from command-line argument

# Command to open Chrome with the specified URL in kiosk mode
command = f'"{chrome_path}" --kiosk {url}'

# Execute the command
subprocess.Popen(command, shell=True)