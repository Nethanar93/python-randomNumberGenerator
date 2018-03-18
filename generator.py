from tkinter import *
from random import randint

root = Tk()

root.title('RandNumGen')

main = Frame(root)
main.pack(padx=10, pady=10)

Label(root, text='Random Number Generator', font=('Helvetica', 20)).pack(in_=main)

input_row = Frame(root)
input_row.pack(in_=main, pady= 5)

Label(root, text='Min: ').pack(in_=input_row, side=LEFT, padx=5)
min = IntVar()
min_entry = Entry(root, relief=SUNKEN, textvariable=min)
min_entry.pack(in_=input_row, side=LEFT, padx=5)
Label(root, text='Max: ').pack(in_=input_row, side=LEFT, padx=5)
max = IntVar()
max_entry = Entry(root, relief=SUNKEN, textvariable=max)
max_entry.pack(in_=input_row, side=LEFT, padx=5)

Label(root, text='Your number:').pack(in_=main)
result = Label(root, text='', font=('Helvetica', 50))
result.pack(in_=main, pady=10)

def generate():
    global min
    global max
    result.config(text=randint(min.get(), max.get()))

Button(root, text='Generate', command=generate).pack(in_=main)


root.mainloop()
