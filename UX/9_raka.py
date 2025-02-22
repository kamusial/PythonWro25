import tkinter as tk
# import customtkinter as ctk
from tkinter.messagebox import showinfo, showerror

def imie():
    msg = f'Wpisałeś: {entry_text.get()}'
    print('Klinięto "IMIE"')
    print(f'Wpisano {msg}')
    showinfo(title='Potwierdzenie', message=f'wpisano imię :{entry_text.get()}')

def comment():
    content = text_field.get('1.0', tk.END)
    # Pobiera tekst od początku ("1.0") do końca (tk.END)
    showerror(title='Pole tekstowe', message=content)

root = tk.Tk()
entry_text = tk.StringVar()
frame = tk.Frame()
frame.pack(padx=50, pady=50)
label = tk.Label(frame, text='Wpisz imie')
label.pack()
entry = tk.Entry(frame, textvariable=entry_text, font=('Helvetica', 20))
entry.pack(ipadx=100, ipady=30)
entry2 = tk.Entry(frame, show='*', font=('Helvetica', 20))
entry2.pack(ipadx=20, ipady=30)
label = tk.Label(frame, text='Wpisz komentarz')
label.pack()
text_field = tk.Text(frame, height=3, width=30)
text_field.pack()
button_entry = tk.Button(frame, text='Złap imie', command=imie)
button_entry.pack(ipadx=5, ipady=5, fill='x')
button_text = tk.Button(frame, text='Złap komentarz', command=comment)
button_text.pack()



root.mainloop()