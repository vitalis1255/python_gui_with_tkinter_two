from tkinter import *

root = Tk()
root.title("Multiple Key Event")
root.geometry("100x100")

btn = Button(root,text="Hover or Click Me")
btn.pack(pady=20)

#create enter event
btn.bind("<Enter>",lambda e: print("Mouse Entered"))

#create leave event
btn.bind("<Leave>",lambda e: print("Mouse Left"))

#create left event
btn.bind("<Button-1>",lambda e: print("Mouse Clicked"))
btn.unbind("<Button-1>")#prevents the button from executing.

root.mainloop()