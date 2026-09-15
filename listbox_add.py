from tkinter import *

root = Tk()
root.title("Listbox Example")
root.geometry("300x300")

def Add_Item():
  Label(root,text=lb.insert(END,entry.get())).pack()
  entry.delete(0,END)

def Delete_single_item():
  selected = lb.curselection()#get current selected item.
  for i in reversed(selected):#reversed is used to avoid index shifting.
    lb.delete(i)

def clear_all():
  lb.delete(0,END)

lb = Listbox(root)

#Add default items
lb.insert(END, "Python")
lb.insert(END, "Java")
lb.pack()

entry = Entry(root)
entry.pack(pady=5)

btn = Button(root, text="Add",command=Add_Item)
btn.pack(pady=5)

del_button = Button(root,text="Delete Item",command=Delete_single_item)
del_button.pack(pady=5)

del_all = Button(root, text="Delete All",command=clear_all)
del_all.pack(pady=5)

root.mainloop()