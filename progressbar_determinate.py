from tkinter.ttk import Progressbar
from tkinter import *

root = Tk()
root.title("Progressbar determinate Example")
root.geometry("300x300")

def Start_progress():
  progess['value'] = 0#initial progress value
  #max_val = 100#initial maximum value
  progess['maximum'] = 100#maximum progress value
  for i in range(100 + 1):#plus 1 to ensure 100 is included.
    progess['value'] = i#update progress value
    progess.update()#refresh update value while progress runs
    root.after(80)#progress running smothly

progess = Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
progess.pack(pady=10)

btn = Button(root, text="Start Progress",command=Start_progress)
btn.pack()

root.mainloop()