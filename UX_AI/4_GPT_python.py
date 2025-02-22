import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


class CSVAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Analyzer")

        # Plik
        self.file_path = tk.StringVar()

        # Opcje pliku
        self.separator = tk.StringVar(value=",")
        self.comment = tk.StringVar(value="#")
        self.selected_column = tk.StringVar()
        self.columns = []

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Wybór pliku
        ttk.Label(frame, text="Plik CSV:").grid(row=0, column=0)
        ttk.Entry(frame, textvariable=self.file_path, width=50).grid(row=0, column=1)
        ttk.Button(frame, text="Wybierz", command=self.load_file).grid(row=0, column=2)

        # Separator
        ttk.Label(frame, text="Separator:").grid(row=1, column=0)
        ttk.Entry(frame, textvariable=self.separator, width=5).grid(row=1, column=1, sticky=tk.W)

        # Komentarz
        ttk.Label(frame, text="Ignoruj komentarze zaczynające się od:").grid(row=2, column=0)
        ttk.Entry(frame, textvariable=self.comment, width=5).grid(row=2, column=1, sticky=tk.W)

        # Analiza pliku
        ttk.Button(frame, text="Analizuj", command=self.analyze_csv).grid(row=3, column=0, columnspan=3)

        # Wybór kolumny do wykresu
        ttk.Label(frame, text="Wybierz kolumnę:").grid(row=4, column=0)
        self.column_menu = ttk.Combobox(frame, textvariable=self.selected_column, state='readonly')
        self.column_menu.grid(row=4, column=1, columnspan=2, sticky=tk.W)

        # Wyjście
        ttk.Button(frame, text="Zamknij", command=self.root.quit).grid(row=5, column=0, columnspan=3)

        # Wyniki analizy
        self.result_text = tk.Text(self.root, height=15, width=80)
        self.result_text.grid(row=1, column=0)

        # Wykresy
        ttk.Button(self.root, text="Pokaż wykresy", command=self.show_plots).grid(row=2, column=0)
        ttk.Button(self.root, text="Zapisz wykres", command=self.save_plot).grid(row=3, column=0)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            self.file_path.set(file_path)
            self.update_columns()

    def analyze_csv(self):
        try:
            df = pd.read_csv(self.file_path.get(), sep=self.separator.get(), comment=self.comment.get())
            summary = df.describe()

            output = StringIO()
            summary.to_string(output)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, output.getvalue())

            self.columns = df.columns.tolist()
            self.column_menu["values"] = self.columns
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można załadować pliku: {str(e)}")

    def show_plots(self):
        try:
            df = pd.read_csv(self.file_path.get(), sep=self.separator.get(), comment=self.comment.get())
            if self.selected_column.get() and self.selected_column.get() in df.columns:
                df[self.selected_column.get()].hist(figsize=(10, 6))
            else:
                df.hist(figsize=(10, 6))
            plt.show()
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można wygenerować wykresów: {str(e)}")

    def save_plot(self):
        try:
            df = pd.read_csv(self.file_path.get(), sep=self.separator.get(), comment=self.comment.get())
            if self.selected_column.get() and self.selected_column.get() in df.columns:
                df[self.selected_column.get()].hist(figsize=(10, 6))
            else:
                df.hist(figsize=(10, 6))
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
            if file_path:
                plt.savefig(file_path)
                messagebox.showinfo("Sukces", "Wykres zapisany pomyślnie!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można zapisać wykresu: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnalyzerApp(root)
    root.mainloop()