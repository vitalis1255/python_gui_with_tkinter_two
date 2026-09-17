from tkinter import *


root = Tk()
root.title("Scale widget")
root.geometry("400x400")

def show_value(val):
  label.config(text=f"selected: {val}")

#scale = Scale(root,from_=0, to=100,orient=HORIZONTAL,command=show_value)
#scale.pack(pady=5)

scale = Scale(root,from_=0, to=10,orient=VERTICAL,resolution=0.5,length=200,tickinterval=2,label="Adjust Value",command=show_value)
scale.pack()

label = Label(root,text="selected: 0")
label.pack()

root.mainloop()