from tkinter import *

def open_modal():
  modal = Toplevel(root)#create a new window
  modal.title("Modal Window")
  modal.geometry("250x120")

  Label(modal,text="Close me before returning to the main window").pack(pady=10)

  Button(modal,text="Close",command=modal.destroy).pack(pady=10)
  modal.grab_set()#captures all events for this window.
  modal.focus_set()#set focus to this window
  modal.wait_window(modal)#pause execution until modal closes. 

root = Tk()#main application window
root.title("Main Window")
root.geometry("300x300")

Button(root,text="Open Modal",command=open_modal).pack(pady=20)

root.mainloop()