import tkinter as tk
from tkinter import filedialog

def Open_File():
  #Open a single file
  file_path = filedialog.askopenfilename(
    title="Open a File",
    filetypes=[("Text Files","*.txt"),("pdf Files","*.pdf"),("Python Files","*.py"),("png Files","*.png"),("All Files","*.*")]
  )
  if file_path:
    tk.Label(root,text=file_path).pack(pady=5)

def open_multiple_file():
  pass

root = tk.Tk()
root.title("File Dialog")
root.geometry("400x200")

#Butt for a single file
tk.Button(root,text="Open File",command=Open_File).pack(pady=5)

#Button for a multiple file
tk.Button(root,text="Open Multiple Files",command=open_multiple_file).pack(pady=5)
root.mainloop() 