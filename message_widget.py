from tkinter import *

root = Tk()
root.title("Message Example")
root.geometry("400x300")


message_text = ("welcome to the Tkinter tutorial."
                   "This message widget automatically wraps long text."
                   "and adjusts the height to fit the content.")

msg = Message(root,text=message_text,width=100,font=("Arial",12),bg="lightblue",fg='black',relief="raised",justify="left",padx=10,pady=10)
msg.pack(pady=20)


root.mainloop()