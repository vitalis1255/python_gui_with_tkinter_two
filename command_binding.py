from tkinter import *

def greet():
  Label(root,text="Hello, Tkinter").pack()

root = Tk()
root.title("Command Binding Example")
root.geometry("200x200")

btn = Button(root,text="Greet",command=greet)
btn.pack()

root.mainloop()