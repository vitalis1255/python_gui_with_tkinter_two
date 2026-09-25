import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("rotate Image")
root.geometry("300x300")

image = Image.open("icons/Waec.jpg")
resize_image = image.resize((50,50))
crop_image = resize_image.rotate(45)#left,upper,right,bottom
get_image = ImageTk.PhotoImage(crop_image)
tk.Label(root,image=get_image).pack(pady=5)



root.mainloop()