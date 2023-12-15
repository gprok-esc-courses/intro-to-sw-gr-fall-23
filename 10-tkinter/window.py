from tkinter import Tk, Button, Label

counter = 0

def button_click():
    global counter
    counter += 1
    c = str(counter)
    label.configure(text=c)



window = Tk()

label = Label(window, text='0')
label.grid(row=1, column=0)

button = Button(window, text="Click Me", command=button_click)
button.grid(row=0, column=0)

window.mainloop()