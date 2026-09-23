import tkinter as tk
from tkinter import messagebox

def new_file():
  title = "Toolbar Action"
  message="New File Created"
  messagebox.showinfo(title=title,message=message)


def open_file():
  title = "Toolbar Action"
  message = "Opne File"
  messagebox.showinfo(title=title,message=message)


root = tk.Tk()
root.title("Toolbar")
root.geometry("400x300")
#----Create Toolbar Frame------
toolbar = tk.Frame(root,bd=1,relief=tk.RAISED)


#load icons (must be .png or .gif)
new_icon = tk.PhotoImage(file="icons/image1.jpg")
open_icon = tk.PhotoImage(file="icons/waec.jpg")


#Add Buttons with Icons
btn_new = tk.Button(root,image=new_icon,command=new_file)
btn_new.pack(side=tk.LEFT,padx=2,pady=2)

btn_open = tk.Button(root,image=new_icon,command=open_file)
btn_open.pack(side=tk.LEFT,padx=2,pady=2)

toolbar.pack(side=tk.TOP,fill=tk.X)
root.mainloop()