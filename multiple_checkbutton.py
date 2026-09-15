from tkinter import *


root = Tk()
root.title("Multiple Checkbutton")
root.geometry("200x300")

def show_selected():
  Label(root,text="Do you like these languages?").pack(side=TOP)
  Label(root,text="Python: " + python_var.get()).pack(pady=5)
  Label(root,text="Java: " + java_var.get()).pack(pady=5)
  Label(root,text="C++: " + cpp_var.get()).pack(pady=5)

#Multiple checkbutton
python_var = StringVar(value="No")#set default value to "No"
java_var = StringVar(value="No")#set default value to "No"
cpp_var = StringVar(value="No")#set default value to "No"

python_checkbutton = Checkbutton(root, text="Python",variable=python_var, onvalue="Yes",offvalue="No")
python_checkbutton.pack(anchor='w')

java_checkbutton = Checkbutton(root, text="Java",variable=java_var, onvalue="Yes",offvalue="No")
java_checkbutton.pack(anchor='w')

c_checkbutton = Checkbutton(root, text="C++",variable=cpp_var, onvalue="Yes",offvalue="No")
c_checkbutton.pack(anchor='w')


Button(root, text="Check Selection",command=show_selected).pack(pady=10)

root.mainloop()