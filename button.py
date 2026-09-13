from tkinter import *

root = Tk()
def button_clicked():
  my_label = Label(root, text="Button clicked")
  my_label.pack()



btn = Button(root,text="button",command=button_clicked)
btn.pack()


root.mainloop()