from tkinter import *

def show_message(string):#string here is the parameter holding or storing argument.
  Label(root,text=f"Hello, {string}").pack()

root = Tk()
root.title("Command Binding Example")
root.geometry("200x200")

btn = Button(root,text="Click Me",command=lambda: show_message("Izuchukwu"))#Izuchukwu here is the argument called a value that is stored in the string parameter.
btn.pack()


root.mainloop()