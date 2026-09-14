from tkinter import *

root = Tk()
root.title("Grid Layout Example")
root.geometry("300x150")

Label(root,text="Username").grid(row=0,column=0,padx=10,pady=5)
Label(root,text="Password").grid(row=1,column=0,padx=10,pady=5)




root.mainloop() 