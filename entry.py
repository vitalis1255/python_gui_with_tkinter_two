from tkinter import *

root = Tk()
root.title("Entry Example")
root.geometry("300x200")

name_var = StringVar()

#Label that also shows what is typed (live update)
label = Label(root,textvariable=name_var,font=("Arial",14),fg="blue")
label.pack(pady=10)

def display():
  label = Label(root, text="Entered Text: " + " " + name_var.get())
  label.pack(pady=10)

  #label = Label(root, text=entry.get())
  #label.pack(pady=20)


entry = Entry(root,textvariable=name_var, font=("Arial",14),width=25,fg="blue",bg="lightyellow",justify="center",relief="groove",bd=2)#show="*" hides what you type.
entry.pack(pady=20)

btn = Button(root, text="Get Text",command=display)
btn.pack(pady=10)

root.mainloop()