from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Notebook Example")
root.geometry("200x200")

#create notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=1,fill='both')

#create tab frames
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

#create labels fro the tabs
Label(tab1,text="Welcome to Tab One").pack(pady=20)
Label(tab2,text="Welcome to Tab Two").pack(pady=20)
Label(tab3,text="Welcome to Tab Three").pack(pady=20)

#Add the tabs to notebook
notebook.add(tab1,text="Tab One")
notebook.add(tab2,text="Tab Two")
notebook.add(tab3,text="Tab Three")

root.mainloop()