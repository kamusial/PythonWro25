import tkinter as tk

root = tk.Tk()
root.title('Pierwszy tkinter')
root.geometry('600x400+1250+100')  #, wymiary i pozycja

message1 = tk.Label(root, text='Witamy we Wrocławiu')
message1.pack()
message2 = tk.Label(root, text='I siema')
message2.pack()
message3 = tk.Label(root, text='..............')
message3.pack()

root.mainloop()
