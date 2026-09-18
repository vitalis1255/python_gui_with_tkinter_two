from tkinter import *

def open_file():
  print("File opened")

def new_file():
  print("New file created")

def exit_file():
  root.quit()

root = Tk()
root.title("Menu Example Two")
root.geometry("300x300")


#create a menu bar
menubar = Menu(root)

#File menu
file_menu = Menu(menubar, tearoff=0)
#create file submenus
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="New",command=new_file)
#Add a horizontal line
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit_file)
#Add file menu to menu bar
menubar.add_cascade(label="File",menu=file_menu)

#Create Edit menu
edit_menu = Menu(menubar, tearoff=0)
#create Edit submenus
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")
#Add Edit menu to menu bar
menubar.add_cascade(label="Edit",menu=edit_menu)

#create help menu
help_menu = Menu(menubar, tearoff=0)
#create about help and let it be inside help_menu
about_menu = Menu(help_menu,tearoff=0)
#create submenus for about_menu
about_menu.add_command(label="Contact Us")
about_menu.add_command(label="About Us")
about_menu.add_command(label="Version Info")
#Add about_menu to the help menu
help_menu.add_cascade(label="About Info",menu=about_menu)
#Add help menu to menu bar
menubar.add_cascade(label="Help",menu=help_menu)

root.config(menu=menubar)
root.mainloop()