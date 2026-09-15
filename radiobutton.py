from tkinter import *


root = Tk()
root.title("Radiobutton Example")
root.geometry("300x300")

def show_selected():
  Label(root, text=radio_var.get()).pack(pady=5)

radio_var = StringVar()
radio_var.set("Male")

radio1 = Radiobutton(root,text="Male",variable=radio_var, value="Male")
radio1.pack()

radio2 = Radiobutton(root,text="Female",variable=radio_var, value="Female")
radio2.pack(pady=5)

Button(root, text="check selection",command=show_selected).pack(pady=5)

root.mainloop()