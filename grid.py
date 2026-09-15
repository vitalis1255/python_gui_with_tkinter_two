from tkinter import *

root = Tk()
root.title("Grid Layout Example")
root.geometry("300x150")

def Show():
  label1 = entry1.get()
  label2 = entry2.get()

  total_label = Label(root, text="Username: " + label1 + " " + "Password: " + " " + label2)
  total_label.grid(row=4,column=0,columnspan=2)
  Label(root, text="Login Successfully...").grid(row=5,column=0,columnspan=2)

  entry1.delete(0,END)
  entry2.delete(0,END)

#Label
Label(root,text="Username:").grid(row=0,column=0,padx=10,pady=5,sticky=E)
Label(root,text="Password:").grid(row=1,column=0,padx=10,pady=5,sticky=E)

#Entry
entry1 = Entry(root, width=30)
entry1.grid(row=0,column=1,pady=5)

entry2 = Entry(root, width=30, show="*")
entry2.grid(row=1,column=1,pady=5)

btn = Button(root, text="Login",bg="yellow",command=Show)
btn.grid(row=2,column=0,columnspan=2,sticky=(W+E),padx=10,pady=10)

exit_button = Button(root, text="Exit",bg="green",fg="white",command=root.destroy)
exit_button.grid(row=3,column=0,columnspan=2,sticky=(W+E),padx=10,pady=10)


root.mainloop() 