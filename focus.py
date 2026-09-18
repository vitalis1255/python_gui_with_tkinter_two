from tkinter import *

def show_focus(event=None):
  current = root.focus_get()
  label.config(text=f"Current focus is on: {current}")

root = Tk()
root.title("Focus Example")
root.geometry("200x200")

entry1 = Entry(root)
entry1.pack(pady=5)
entry2 = Entry(root)
entry2.pack(pady=5)
entry3 = Entry(root)
entry3.pack(pady=5)

#set focus on entry 2
btn = Button(root,text="Focus Entry 2",command=lambda: entry2.focus_set())#lambda tells Button to focus on entry 2
btn.pack(pady=5)

root.bind("<Key>",show_focus)

#set focus on entry 1
entry1.focus_set()
#set focus on entry 3
entry3.focus_set()

label = Label(root,text=" ")
label.pack()

root.mainloop()