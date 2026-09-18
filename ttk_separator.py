from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Separator Example")
root.geometry("200x200")

Label(root,text="Above the line").pack()  
ttk.Separator(root,orient='horizontal').pack(fill='x',pady=10)
Label(root,text="Below the line").pack()

root.mainloop()