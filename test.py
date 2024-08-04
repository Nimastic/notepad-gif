import subprocess
import os
import platform

def open_notepad():
    if platform.system() == "Windows":
        subprocess.Popen(['notepad.exe'])
    else:
        print("This script is designed for Windows OS.")

def open_minecraft():
    minecraft_path = "C:\\Path\\To\\Minecraft\\Launcher.exe"  # Change this to the path of your Minecraft launcher

    if os.path.exists(minecraft_path):
        subprocess.Popen([minecraft_path])
    else:
        print("Minecraft path is not valid. Please check the path to the Minecraft executable.")

if __name__ == "__main__":
    open_notepad()
    open_minecraft()
