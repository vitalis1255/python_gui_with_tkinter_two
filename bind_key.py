from tkinter import *

def on_key(event):
  label.config(text=f"Key Pressed: {event.char} | Symbol: {event.keysym} ")

root = Tk()
root.title("Keyboard Example")
root.geometry("200x200")

entry = Entry(root)
entry.pack(pady=20)


entry.bind("<Key>",on_key)#Press any key

label = Label(root, text=" ")
label.pack()

root.mainloop()