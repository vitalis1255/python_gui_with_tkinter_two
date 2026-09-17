#from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.title("Combobox Example")
root.geometry("200x200")

def show_selected():
  selected = combo.get()
  label.config(text=f"You selected: {selected}")

items = ["FirstName","MiddleName","LastName","Age","State","Country"]
combo = Combobox(root,values=items,state='readonly')
combo.current(0)#set the current value
combo.set("LGA")#add it to the items list
combo.pack(pady=10)

label = Label(root,text=" ")
label.pack() 

btn = Button(root, text="Show Selected",command=show_selected)
btn.pack(pady=5)




root.mainloop()