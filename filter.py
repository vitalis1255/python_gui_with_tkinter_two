import tkinter as tk
from PIL import Image,ImageTk,ImageFilter,ImageOps

root = tk.Tk()
root.title("filter Image")
root.geometry("300x300")

image = Image.open("icons/Waec.jpg")
resize_image = image.resize((50,50))

#crop_image = ImageOps.grayscale(resize_image)

crop_image = resize_image.filter(ImageFilter.BLUR)
get_image = ImageTk.PhotoImage(crop_image)
tk.Label(root,image=get_image).pack(pady=5)



root.mainloop()