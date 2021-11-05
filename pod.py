#!/usr/bin/python3
# -*- coding: utf-8 -*-


import tkinter as tk
import threading
import imageio
from PIL import ImageTk
from PIL import Image
from playsound import playsound


playsound("./syno_gif/minipodcom.mp4")
video_name = "./syno_gif/minipodcom.mp4"
video = imageio.get_reader(video_name)

def stream(label):
    """
        main frame
    """
    for image in video.iter_data():
        image_frame = Image.fromarray(image)
        frame_image = ImageTk.PhotoImage(image_frame)
        label.config(image=frame_image)
        label.image = frame_image
        root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.destroy()
