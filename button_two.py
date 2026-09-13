import tkinter as tk


root = tk.Tk()
root.title("Button")
root.geometry("300x300")

def button_clicked():
  label.config(text="Button clicked")#replaces Press the button below when clicked.

label = tk.Label(root,text="Press the button below",font=("Arial",14))
label.pack(pady=10)

button_frame = tk.Frame(root, width=200,height=200,borderwidth=5, relief=tk.RAISED)
button_frame.pack(pady=20,padx=20,fill=tk.BOTH,expand=True)

btn = tk.Button(button_frame, text="Click Button",command=button_clicked,font=("Arial",12),bg="blue",fg="black")
btn.pack(pady=20)

root.mainloop()