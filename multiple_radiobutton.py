from tkinter import *


root = Tk()
root.title("Multiple Radiobutton")
root.geometry("300x300")

def show_selection():
  Label(root,text=choice.get()).pack(pady=5)

choice = StringVar()
choice.set("option 1")

#Multiple radiobutton
Radiobutton(root, text="option 1",variable=choice, value="option 1").pack()#what displays is value.
Radiobutton(root, text="option 2",variable=choice, value="option 2").pack(pady=5)#what displays is value.
Radiobutton(root, text="option 3",variable=choice, value="option 3").pack(pady=5)#what displays is value.

Button(root, text="submit",command=show_selection).pack(pady=5)

root.mainloop()