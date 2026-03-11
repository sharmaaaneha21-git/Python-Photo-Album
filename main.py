import tkinter as tk
import time
from PIL import Image, ImageTk

# ------------------Main Window---------------------------

root= tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of Image path
image_paths= [
    r"C:\Users\nehan\Desktop\Album\img1.jpeg",         
    r"C:\Users\nehan\Desktop\Album\img2.jpeg",
    r"C:\Users\nehan\Desktop\Album\img3.jpeg",
    r"C:\Users\nehan\Desktop\Album\img4.jpeg",
    r"C:\Users\nehan\Desktop\Album\img5.jpeg",
    r"C:\Users\nehan\Desktop\Album\img6.jpeg"
]
image_size = (400, 400)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)          #adding each images in the list

# convert PIL image into Tkinter friendly compatible image
final_images= []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)


# Slideshow function
def start_slideshow():
    for photo in final_images:
        image_label.config(image = photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

# Button
play_button = tk.Button(
    root,
    text = "Play the Slideshow",
    font = ("Arial", 17),
    command = start_slideshow
)
play_button.pack(pady=40)


root.mainloop()