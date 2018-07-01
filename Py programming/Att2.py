from tkinter import Label,Button,Tk,mainloop
#Define the callback function invoked when button is pressed
def hello_callback():print ("Greatly Blessed")
top=Tk()
top.title("GreHiDeL MwEnDwA")
top.minsize(600,600)
top.configure(bg="Purple")
#Make a label
Label(text="GreHiDeL").pack()
# Make a button
b=Button(text="What does G mean?",command=hello_callback)
b.pack()
mainloop()
