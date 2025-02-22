import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

def clicked():
    showinfo(title='Info', message='kliknięto')

root = tk.Tk()
img = Image.open('piesek.jpg')
img_resized = img.resize((100, 100), Image.ADAPTIVE)
photo = ImageTk.PhotoImage(img_resized)
button = tk.Button(
    text='Przycisk',
    fg='red',
    bg='#609465',
    font=('Arial', 24),
    image=photo,
    compound=tk.TOP,
    command=clicked
)
button.pack(ipadx=15, ipady=10)

root.mainloop()
