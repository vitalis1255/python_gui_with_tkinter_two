from tkinter import *

def draw(event):
  x,y = event.x,event.y#create origin of x,y
  canvas.create_line(x,y,x+1,y+1, fill=current_color[0],width=3)#x,y is the origin, while x+1,y+1 is the end.

def change_color(event):
  key = event.char.lower()
  colors = {
    'r':'red',
    'g':'green',
    'b':'blue',
    'y':'yellow',
    'p':'purple',
    'o':'orange',
    'k':'black',
    'l':'lightblue'
  }

  if key in colors:
    current_color[0] = colors[key]
    status_label.config(text=f"current color: {current_color[0]}")
  else:
    status_label.config(text=f"Unknown key: {event.char}")#name of key pressed.

root = Tk()#main window
root.title("Draw & Change Colors with bind()")
root.geometry("500x400")#width=500,height=400

#Create Canvas for drawing
canvas = Canvas(root,bg="white",width=480,height=320)
canvas.pack(pady=10)

#status label
status_label = Label(root,text="Current Color: black")
status_label.pack()

#Store current color in a mutable list so it can be changed in function.
current_color = ["black"]

#Bind mouse drag to draw
canvas.bind("<B1-Motion>",draw)
root.bind("<Key>",change_color)


root.mainloop()