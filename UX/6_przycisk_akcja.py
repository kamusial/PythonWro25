import tkinter as tk

def hello_message():
    print('Siema')

root = tk.Tk()
root.attributes('-alpha', 0.8)  # nieprzeźroczystość
root.attributes('-topmost', 1)  # onko zawsze na wierzchu

message1 = tk.Label(root, text='Witamy we Wrocławiuuuuuuuuu')
message1.pack()
message2 = tk.Label(root, text='I siema')
message2.pack()
message3 = tk.Label(root, text='..............')
message3.pack()

button_hello = tk.Button(root, text='Hello', command=hello_message, anchor='e')
button_hello.pack(padx=5, pady=50)
button_exit = tk.Button(root, text='Quit', command=root.quit, anchor='s')
button_exit.pack(ipadx=50, ipady=15)  # wewnętrzne rozszerzenie
message4 = tk.Label(root, text='')
message4.pack()



root.mainloop()
