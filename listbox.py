from tkinter import *

root = Tk()
root.title("Listbox Example")
root.geometry("300x300")

def show_selection():
  selected = lb.get(ACTIVE)#An item selected becomes active.
  Label(root,text="Selected: " + selected).pack()


lb = Listbox(root)
lb.insert(1, "Python")#index 1
lb.insert(2, "Java")#index 2
lb.insert(3, "C++")#index 3
lb.insert(4, "Javascript") #index 4

lb.pack()

btn = Button(root, text="Show",command=show_selection)
btn.pack(pady=5)

root.mainloop()