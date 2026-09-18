from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Panedwindow")
root.geometry("200x200")

#create PanedWindow
pw = ttk.PanedWindow(root,orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=1)

#create two labels(left and right labels)
left = Label(root,text="Left Pane",bg="lightgreen")
right = Label(root,text="Right",bg="purple")

#Add them to panedwindow
pw.add(left)
pw.add(right)

root.mainloop()