import tkinter as tk
root = tk.Tk()
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.9)
root.geometry('500x600+1350+100')
root.title('moj program')

label = tk.Label(root, text='Kalkulator', font=('Arial', 20),
                background='#265ECE', fg='red')
label.pack(padx=20, pady=20)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=10)
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
# buttonframe.rowconfigure

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2)


buttonframe.pack()




root. mainloop()