from tkinter import *
from tkinter import ttk


root = Tk()#main window
root.title("Notebook Example")
root.geometry("200x200")

#create notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=1,fill='both')

#create two tabs Frame
tab1 = Frame(notebook)#notebook is a window of its own.
tab2 = Frame(notebook)

#create labels for tab1 and tab2
Label(tab1, text="welcome to tab 1").pack(pady=20)
Label(tab2, text="welcome to tab 2").pack(pady=20)

notebook.add(tab1, text="Tab One")
notebook.add(tab2,text="Tab Two")

root.mainloop()