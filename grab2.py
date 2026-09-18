from tkinter import *

def lock_events():
  btn.grab_set() 
  status.config(text="Grab is active: Clicks only work on this button")

def release_events():
  btn.grab_release()
  status.config(text="Grab is released: You can click anywhere")

root = Tk()
root.title("Another approach for Grab")
root.geometry("400x400")

btn = Button(root,text="Click Me")
btn.pack(pady=10)

Button(root,text="Grab Events",command=lock_events).pack() 
Button(root,text="Release Events",command=release_events).pack() 

status = Label(root,text="No grab active")
status.pack(pady=10)

root.mainloop()