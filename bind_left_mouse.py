from tkinter import *



def on_click(event):
  label.config(text=f"Mouse clicked at: ({event.x},{event.y})")

root = Tk()
root.title("Bind Left Mouse Click")
root.geometry("400x200")

#create a label
label = Label(root,text="Click inside me",bg="lightblue",width=30,height=5)
label.pack(pady=20)

#bind the label
label.bind("<Button-1>",on_click)#Left mouse click event

root.mainloop()