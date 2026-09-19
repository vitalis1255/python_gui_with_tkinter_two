import tkinter as tk

def show_values():
  str_value = str_var.get()
  int_value = int_var.get()
  dbl_value = double_var.get()
  bool_value = bool_var.get()

  print(f"String: {str_value}")
  print(f"Integer: {int_value}")
  print(f"Double: {dbl_value}")
  print(f"Boolean: {bool_value}")

root = tk.Tk()
root.title("All Variable Types Example")
root.geometry("580x400")

#Variables
str_var = tk.StringVar(value="Hello")#Assign default value
int_var = tk.IntVar(value=10)#Assign default value
double_var = tk.DoubleVar(value=3.14)#Assign default value
bool_var = tk.BooleanVar(value=True)#Assign default value

#widget to bound the variables
tk.Entry(root,textvariable=str_var).pack()
tk.Spinbox(root, from_=10, to=100, textvariable=int_var).pack()
tk.Entry(root,textvariable=double_var).pack()
tk.Checkbutton(root,text="Agree",variable=bool_var).pack()

tk.Button(root,text="Show values",command=show_values).pack()

label =tk.Label(root, text=" ")
label.pack()

root.mainloop()