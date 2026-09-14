from tkinter import *

root = Tk()
root.title("Text Widget Example")
root.geometry("400x300+200+50")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)

def fetch():
  content = text.get("1.0",END)#1.0 line 1 and 0 for texts to get
  label = Label(root, text="User Input: " + content)
  label.pack(pady=10)

text = Text(root,
            yscrollcommand=scroll.set,
            height=10,
            width=40,
            font=("Arial",12),
            fg="blue",bg="yellow",
            wrap="word",relief="groove",
            borderwidth=2)
text.pack(pady=20)
scroll.config(command=text.yview)


btn = Button(root,text="Fetch Text",command=fetch)
btn.pack(pady=10)
root.mainloop()