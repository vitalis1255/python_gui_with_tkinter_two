import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Crop Image")
root.geometry("300x300")

image = Image.open("icons/Waec.jpg")
crop_image = image.crop((50,50,250,250))#left,upper,right,bottom
get_image = ImageTk.PhotoImage(crop_image)
tk.Label(root,image=get_image).pack(pady=5)



root.mainloop()