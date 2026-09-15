from tkinter import *

root = Tk()
root.title("Nested Layouts Example")
root.geometry("400x300")

# Frame 1 (top)
top_frame = Frame(root, bg="lightblue",height=100)
top_frame.pack(fill=X)

label_top = Label(top_frame, text="Top Frame",bg="lightblue")
label_top.pack(pady=10)

#Frame 2 (bottom), contains a grid layout
bottom_frame = Frame(root, bg="lightgray")
bottom_frame.pack(fill=BOTH,expand=True)

#nested frame inside bottom_frame for form fields
nested_frame = Frame(bottom_frame,bg="lightgray")
nested_frame.pack(pady=20)

Label(nested_frame,text="Name:",bg="lightgray").grid(row=0,column=0,padx=10,pady=5,sticky=E)
Entry(nested_frame).grid(row=0,column=1,padx=10,pady=5)


Label(nested_frame, text="Password:",bg="lightgray").grid(row=1,column=0,padx=10,pady=5,sticky=E)
Entry(nested_frame).grid(row=1,column=1,padx=10,pady=5)

Button(nested_frame, text="Submit",bg="green",fg="white").grid(row=2,column=0,columnspan=2,pady=10,sticky=(W+E))

root.mainloop()