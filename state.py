from tkinter import *

def toggle_button():
  if btn["state"] == NORMAL:
    btn.config(state=DISABLED,text="Disabled")
  else:
    btn.config(state=NORMAL,text="Enabled")

root = Tk()
root.title("State")
root.geometry("300x300")

btn = Button(root,text="Enabled",command=lambda: print("Button Clicked!"))#lambda prints Button Clicked
btn.pack(pady=10)

toggle_btn = Button(root,text="Enable/Disable",command=toggle_button)
toggle_btn.pack(pady=10)

root.mainloop()