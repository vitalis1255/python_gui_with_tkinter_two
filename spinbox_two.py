from tkinter import *


root = Tk()
root.title("Spinbox Second Example")
root.geometry("200x200")

def spin_box():
  selected_value = spin.get()
  label.config(text=f"Current value: {selected_value}")

spin = Spinbox(root, from_=0,to=7,state='readonly',command=spin_box)#button spinbox
spin.pack(pady=5)

label = Label(root, text="Current value: ")
label.pack(pady=5)


root.mainloop()