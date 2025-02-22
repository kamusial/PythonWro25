import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Data Analyzer")
        self.file_path = None

        # Elementy UI
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.load_button = tk.Button(self.frame, text="Load CSV", command=self.load_csv)
        self.load_button.pack(side=tk.LEFT, padx=10)

        self.save_button = tk.Button(self.frame, text="Save Data", command=self.save_data)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.plot_button = tk.Button(self.frame, text="Plot Data", command=self.plot_data)
        self.plot_button.pack(side=tk.LEFT, padx=10)

        self.separator_label = tk.Label(self.frame, text="Separator:")
        self.separator_label.pack(side=tk.LEFT, padx=5)

        self.separator_entry = tk.Entry(self.frame, width=5)
        self.separator_entry.pack(side=tk.LEFT, padx=5)
        self.separator_entry.insert(0, ',')  # Default separator

        self.comment_label = tk.Label(self.frame, text="Comment Char:")
        self.comment_label.pack(side=tk.LEFT, padx=5)

        self.comment_entry = tk.Entry(self.frame, width=5)
        self.comment_entry.pack(side=tk.LEFT, padx=5)
        self.comment_entry.insert(0, '#')  # Default comment character

        self.text = tk.Text(self.root, height=10)
        self.text.pack(pady=20)

    def load_csv(self):
        options = {'defaultextension': '.csv', 'filetypes': [('CSV files', '.csv'), ('All files', '*.*')]}
        self.file_path = filedialog.askopenfilename(**options)
        if self.file_path:
            try:
                self.df = pd.read_csv(self.file_path,
                                      sep=self.separator_entry.get(),
                                      comment=self.comment_entry.get())
                self.text.insert(tk.END, str(self.df.describe()) + '\n')
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.df = None

    def plot_data(self):
        if self.df is not None:
            try:
                fig = plt.figure(figsize=(6, 4))
                ax = fig.add_subplot(111)
                self.df.plot(ax=ax)
                plt_canvas = FigureCanvasTkAgg(fig, self.root)
                plt_canvas.get_tk_widget().pack()
                plt_canvas.draw()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Data not loaded")

    def save_data(self):
        if self.df is not None:
            options = {'defaultextension': '.csv', 'filetypes': [('CSV files', '.csv'), ('All files', '*.*')]}
            file_path = filedialog.asksaveasfilename(**options)
            if file_path:
                try:
                    self.df.to_csv(file_path, index=False)
                    messagebox.showinfo("Saved", "Data saved successfully")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "No data to save")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
