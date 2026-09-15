from tkinter import *

root = Tk()
root.title("Place Widget Example")
root.geometry("300x200")

#Absolute positioning
btn1 = Button(root, text="Button 1")
btn1.place(x=20,y=30)

#Relative positioning
btn2 = Button(root, text="Button 2")
btn2.place(relx=0.8,rely=0.5,anchor='center')
root.mainloop()