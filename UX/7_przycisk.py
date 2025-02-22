import tkinter as tk
from tkinter.messagebox import showinfo

def clicked():
    showinfo(title='Info', message='kliknięto')

root = tk.Tk()
icon = tk.PhotoImage(file='piesek.png')
icon_small = icon.subsample(5, 5)
button = tk.Button(
    text='Przycisk',
    fg='red',
    bg='#609465',
    font=('Arial', 24),
    image=icon_small,
    compound=tk.TOP,
    command=clicked
)
button.pack()

root.mainloop()
