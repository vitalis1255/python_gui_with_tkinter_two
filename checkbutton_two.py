from tkinter import *


root = Tk()
root.title("Checkbutton Example Two Using onvalue and offvalue")
root.geometry("300x300")

def Check_state():
  Label(root, text="Current value: " + var.get()).pack(pady=10)

var = StringVar(value="No")#set default to "No"

Checkbutton(root, text="I agree to the terms and conditions",variable=var,onvalue="Yes",offvalue="No").pack()

Button(root,text="Check State",command=Check_state,bg="red").pack(pady=10)

root.mainloop()