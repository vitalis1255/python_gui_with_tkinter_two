import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messagebox Example")
root.geometry("200x200")

def Message():
  messagebox.showerror(title=title,message=message,detail=details)
  

title = "Error"
message = "Check info entered"
details = "TypeError occured due to incomplete information provided in the Entry filed"

btn = tk.Button(root,text="Show Message",command=Message)
btn.pack(pady=5)

root.mainloop()