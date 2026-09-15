from tkinter import *

root = Tk()
root.title("Listbox Multiple Example")
root.geometry("300x300")

def show_selection():
  indices = lb.curselection()#current selected item.
  selected_item = [lb.get(i) for i in indices]# list comprehension
  Label(root,text=selected_item).pack()


lb = Listbox(root,selectmode=MULTIPLE)

languages = ["Python","Java","C++","Javascript","Go"]
for lang in languages:
  lb.insert(END, lang)#END is an index(at the end of the list)
lb.pack()


btn = Button(root, text="Show",command=show_selection)
btn.pack(pady=5)

root.mainloop()