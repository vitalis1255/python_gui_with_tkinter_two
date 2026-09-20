import tkinter as tk

def on_text_change(*args):#args to avoid any external parameter.
  label.config(text=f"Current value: {text_var.get()}")

root = tk.Tk()
root.title("Real-Time Updates with trace_add")
root.geometry("580x400")

text_var = tk.StringVar(value="")
entry = tk.Entry(root,textvariable=text_var,width=30)
entry.pack(pady=5)

label = tk.Label(root,text="Type Something above...",font=("Arial",14))
label.pack(pady=5)

#How to use trace_add
text_var.trace_add("write",on_text_change)

root.mainloop()