from tkinter.ttk import Progressbar
from tkinter import *

root = Tk()
root.title("Progressbar indeterminate Example")
root.geometry("200x100")

def run_indeterminate():
  progess.start(10)#start every 10 mins interval

def stop_indeterminate():
  progess.stop()

progess = Progressbar(root,orient=HORIZONTAL,length=300,mode='indeterminate')
progess.pack(pady=10)

Button(root, text="Start Loading",command=run_indeterminate).pack()
Button(root, text="Stop",command=stop_indeterminate).pack()

root.mainloop()