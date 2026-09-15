from tkinter import *


root = Tk()
root.title("Checkbutton Example")
root.geometry("300x300")

def check_button():
  Label(root, text="Checked: " if  var.get() else "Unchecked").pack()

var = IntVar()

Checkbutton(root, text="Option 1", variable=var).pack()

Button(root, text="Check", command=check_button).pack(pady=10)


root.mainloop()