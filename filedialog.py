import tkinter as tk
from tkinter import filedialog

#Display a single file path
#single file
def Open_File():
  #Open a single file to get the file path
  file_path = filedialog.askopenfilename(
    title="Open a File",
    filetypes=[("Text Files","*.txt"),("pdf Files","*.pdf"),("Python Files","*.py"),("png Files","*.png"),("All Files","*.*")]
  )
  if file_path:
    tk.Label(root,text=file_path).pack(pady=5)

  with open(file_path,'r', encoding='utf-8') as file:
    tk.Label(root, text=file.read()).pack()#still checking

#Display the path of multiple files
#multiple files
def open_multiple_file():
  files = filedialog.askopenfilenames(
    title="Open Multiple Files",
    filetypes=[("Images","*.png","*.jpg","*.jpeg","*.ai","*.psd"),("All Files","*.*")]
  )
  if files:
    tk.Label(root,text=files).pack(pady=5)

#save file function
#Display save file path
def save_file():
  save_path = filedialog.asksaveasfilename(
    title="Save as",
    defaultextension=".txt",#default for saving the file
    filetypes=[("Text Files","*.txt"),("All Files","*.*")]
  )
  if save_path:
    tk.Label(root,text="File saved at:" + " " + save_path).pack(pady=5)

#Display folder path
def select_folder():
  folder = filedialog.askdirectory(
    title="Select a Folder",
  )
  if folder:
    tk.Label(root,text=folder).pack(pady=5)

#exit tkinter
def exit_app():
  root.destroy()

root = tk.Tk()
root.title("File Dialog Example")
root.geometry("400x200")

#Butt for a single file
tk.Button(root,text="Open a single File",command=Open_File).pack(pady=5)

#Button for a multiple file
tk.Button(root,text="Open Multiple Files",command=open_multiple_file).pack(pady=5)

#Exit App
tk.Button(root,text="Exit",command=exit_app).pack(pady=5)

#save file button
tk.Button(root,text="Save File",command=save_file).pack(pady=5)

#file directory button
tk.Button(root,text="Select Folder",command=select_folder).pack(pady=5)

root.mainloop() 