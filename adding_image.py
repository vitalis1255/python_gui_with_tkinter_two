import tkinter as tk
from PIL import Image,ImageTk

def img_open():
  img = Image.open("icons/image1.jpg")
  img_resize = img.resize((50,50))
  img_resized = ImageTk.PhotoImage(img_resize)
  tk.Label(root,image=img_resized).pack()

root=tk.Tk()
root.title("Load Image")
root.geometry("400x300")

tk.Button(root,text="Show Image").pack()


root.mainloop()