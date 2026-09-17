from tkinter import *

root = Tk()
root.title("Spinbox Example")
root.geometry("200x200")

def spin_box():
  selected = spin.get()
  selected_days = spin2.get()
  label.config(text=f"You selected: {selected}, which is: {selected_days}")

#using spinbox for numbers
spin = Spinbox(root, from_=0,to=7,increment=1,state='readonly')
spin.pack()

#using spinbox for strings,use tuple bracket or list bracket.
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")#tuple
spin2 = Spinbox(root, values=days,state='readonly')
spin2.pack(pady=5)

label = Label(root, text=" ")
label.pack(pady=5)

btn = Button(root, text="Show Spinbox", command=spin_box)
btn.pack(pady=5)


root.mainloop()