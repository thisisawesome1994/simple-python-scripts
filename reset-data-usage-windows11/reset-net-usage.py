import subprocess
import time

def reset_data_usage():
    # Execute the netsh command to reset network interface statistics
    subprocess.run(['netsh', 'interface', 'ip', 'reset'])

    print("Data usage reset.")

# Reset data usage
if __name__ == '__main__':
    reset_data_usage()
    time.sleep(3600)
