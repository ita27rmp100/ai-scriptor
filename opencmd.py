import subprocess
import sys

def open_cmd_and_run(command):
    if sys.platform != "win32":
        print("This script can only open CMD on Windows.")
        return

    try:
        subprocess.Popen(["cmd", "/k", command], shell=True)
        print(f"CMD opened and ran: {command}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    open_cmd_and_run("dir")
