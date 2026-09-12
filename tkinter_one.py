import tkinter as tk


#How to exit full screen
def exit_fullscreen(event=None):
  root.attributes('-fullscreen',False)

root = tk.Tk()#This creates the main window
root.title("First tkinter")
root.geometry("400x400+400+100")#plus 200 x-offset shift tkinter window to left while plus 300 y-offset shift tkinter window down
root.iconbitmap("mypic.ico")#used to change tkinter icon
#root.resizable(width=False,height=False)
#root.minsize(width=400,height=300)#minimumsize of the window
#root.maxsize(width=1200,height=800)#maxsize of the window
#root.attributes('-fullscreen',True)#set transpanrency level.This creates full window.

root.attributes('-fullscreen',True)

#How to bind the full screen
root.bind('<Escape>',exit_fullscreen)

root.mainloop()#Runs the application