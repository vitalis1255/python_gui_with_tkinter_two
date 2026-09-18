from tkinter import *

def new_file():
  print("New file created.")

def open_file():
  print("File opened.")

def exit_app():
  root.quit()
  print("Exit File successful")

def copy_file():
  print("File copied")

def cut_file():
  print("File cut.")

def paste_file():
  print("File pasted")

root = Tk()
root.title("Menu Example")
root.geometry("300x300")

#create a menu using Menu() object
menubar = Menu(root)

#File menu
file_menu = Menu(menubar, tearoff=0)

#Add submenu using add_command(label,command)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
#create a horizontal line using add_separator
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_app)
#Add file menu to the menubar
menubar.add_cascade(label="File",menu=file_menu)

#Edit menu
edit_menu = Menu(menubar, tearoff=0)
#Add Edit submenus
edit_menu.add_command(label="Copy",command=copy_file)
edit_menu.add_command(label="Cut",command=cut_file)
edit_menu.add_command(label="Paste",command=paste_file)
#Add Edit_menu to menu bar
menubar.add_cascade(label="Edit",menu=edit_menu)

#Help menu
help_menu = Menu(menubar, tearoff=0)
about_menu = Menu(help_menu, tearoff=0)
about_menu.add_command(label="About")
about_menu.add_command(label="Version Info")
help_menu.add_cascade(label="About",menu=about_menu)#create About with arrow that contains About and Version Info
#Add help_menu to menu bar
menubar.add_cascade(label="Help",menu=help_menu)

#view menu
view_menu = Menu(menubar,tearoff=0)

#Add view_menu to Menu bar
menubar.add_cascade(label="View",menu=view_menu)

#Add Menu to the main window
root.config(menu=menubar)

root.mainloop()