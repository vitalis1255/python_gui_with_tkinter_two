from tkinter import *

#toggle callback function
def toggle_events():
  if btn["state"] == NORMAL:
    btn.config(state=DISABLED,text="Disabled")
  else:
    btn.config(state=NORMAL,text="Enabled")

root = Tk()
root.title("state enabled/disabled")
root.geometry("100x100")

#create button to be toggled
btn = Button(root, text="Enabled",command=lambda: print("Button Clicked"))
btn.pack(pady=10)

#create toggle button
toggle_button = Button(root,text="Enable/Disable",command=toggle_events)
toggle_button.pack(pady=10)

root.mainloop()