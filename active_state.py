from tkinter import *

root = Tk()#main window
root.title("Active state Hovering")
root.geometry("300x300")

btn = Button(root, text="Hover Me", bg="blue",activebackground="lightgreen")#when the button is clicked,activebacground changes the color to lightgreen.
btn.pack(pady=20)

root.mainloop()