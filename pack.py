from tkinter import *

root = Tk()
root.title("Pack Example")
root.geometry("300x200")

#using side
"""
btn1 = Button(root,text="Top Button",bg="lightblue")
btn2 = Button(root,text="Left Button",bg="lightgreen")
btn3 = Button(root,text="Right Button",bg="lightpink")

btn1.pack(side=TOP,fill=X)
btn2.pack(side=LEFT,fill=Y)
btn3.pack(side=RIGHT,fill=Y)
"""

#using expand
btn1 = Button(root,text="Top",bg="lightblue")
btn2 = Button(root,text="Bottom",bg="lightgreen")

#expand true makes the button to stretch
#btn1.pack(side=TOP,fill=BOTH,expand=True)
#btn2.pack(side=BOTTOM,fill=BOTH,expand=True)

btn1.pack(side=TOP,fill=X,expand=False)
btn2.pack(side=TOP,fill=X,expand=False)

#Run the application
root.mainloop()