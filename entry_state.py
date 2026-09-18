from tkinter import *

def lock_unlock():
  if entry["state"] == NORMAL:
    entry.config(state=DISABLED)
    label.config(text="Enable Entry")
  else:
    entry.config(state=NORMAL)
    label.config(text="Disable Entry")

root = Tk()#main window
root.title(" Entry state enabled/disabled")
root.geometry("300x300")

entry = Entry(root)
entry.pack(pady=5)

btn = Button(root, text="Lock Entry",command=lock_unlock)
btn.pack(pady=5)

label = Label(root,text=" ")
label.pack(pady=5)

root.mainloop()