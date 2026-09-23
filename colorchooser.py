import tkinter as tk
from tkinter import colorchooser

def choose_color():
  color = colorchooser.askcolor(title="Pick a color")
  if color[1]:
    tk.Label(root,text="RGB:" + " " + str(color[0])).pack(pady=5)
    tk.Label(root,text="Hex:" + " " + str(color[1])).pack(pady=5)

    #Use color picked to change background tkinter window
    root.config(bg=color[1])

root = tk.Tk()
root.title("colorchooser")
root.geometry("300x200")

tk.Button(root,text="Choose Color",command=choose_color).pack(pady=10)


root.mainloop()