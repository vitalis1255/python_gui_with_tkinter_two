from tkinter import *


root=Tk()
root.title("PanedWindow Example")
root.geometry("200x200")

pw = PanedWindow(root,orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=1)
left = Label(pw,text="Left Pane",bg="lightblue")
#Add to panedwindow
pw.add(left)

right = Label(pw,text="Right Pane",bg="lightgreen")
pw.add(right)

root.mainloop()