import subprocess
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

def open_notepad():
    subprocess.Popen(['notepad.exe'])

def display_gif():
    root = tk.Tk()
    root.title("Display GIF")
    
    # Load the GIF using PIL
    gif_path = "your_gif_path.gif"  # Change this to the path of your GIF file
    gif = Image.open(gif_path)
    frames = []

    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass

    def update_frame(index):
        frame = frames[index]
        gif_label.config(image=frame)
        root.after(100, update_frame, (index + 1) % len(frames))  # Update frame every 100 ms

    gif_label = Label(root)
    gif_label.pack()

    root.after(0, update_frame, 0)

    root.mainloop()

if __name__ == "__main__":
    open_notepad()
    display_gif()
