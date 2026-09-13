from tkinter import *

root = Tk()
root.title("Frame")
root.geometry("700x300")

frame = Frame(root,borderwidth=5,relief="groove")
frame.pack(padx=10,pady=10,side=LEFT,fill="y")

my_label = Label(frame,text="You are welcome",fg="red",bg="gray")
my_label.pack()


root.mainloop()