import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CSVAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Analyzer")
        self.df = None
        self.fig = None  # przechowuje ostatnio wygenerowany wykres

        # Ramka ustawień – wczytywanie pliku i opcje pliku CSV
        options_frame = tk.Frame(root)
        options_frame.pack(pady=10)

        # Przycisk wczytania pliku CSV
        self.btn_load = tk.Button(options_frame, text="Wczytaj CSV", command=self.load_csv)
        self.btn_load.grid(row=0, column=0, padx=5)

        # Separator
        tk.Label(options_frame, text="Separator:").grid(row=0, column=1, padx=5)
        self.entry_separator = tk.Entry(options_frame, width=5)
        self.entry_separator.grid(row=0, column=2, padx=5)
        self.entry_separator.insert(0, ",")

        # Znak komentarza
        tk.Label(options_frame, text="Komentarz:").grid(row=0, column=3, padx=5)
        self.entry_comment = tk.Entry(options_frame, width=5)
        self.entry_comment.grid(row=0, column=4, padx=5)
        self.entry_comment.insert(0, "#")

        # Kodowanie
        tk.Label(options_frame, text="Encoding:").grid(row=0, column=5, padx=5)
        self.entry_encoding = tk.Entry(options_frame, width=10)
        self.entry_encoding.grid(row=0, column=6, padx=5)
        self.entry_encoding.insert(0, "utf-8")

        # Ramka przycisków analizy i zapisu danych/statystyk
        action_frame = tk.Frame(root)
        action_frame.pack(pady=5)

        self.btn_analyze = tk.Button(action_frame, text="Analiza danych", command=self.analyze_data)
        self.btn_analyze.grid(row=0, column=0, padx=5)

        self.btn_save_csv = tk.Button(action_frame, text="Zapisz dane", command=self.save_csv)
        self.btn_save_csv.grid(row=0, column=1, padx=5)

        self.btn_save_stats = tk.Button(action_frame, text="Zapisz statystyki", command=self.save_stats)
        self.btn_save_stats.grid(row=0, column=2, padx=5)

        # Pole tekstowe do wyświetlania statystyk
        self.text_stats = tk.Text(root, height=15, width=100)
        self.text_stats.pack(pady=10)

        # Ramka opcji wykresu
        plot_options_frame = tk.Frame(root)
        plot_options_frame.pack(pady=10)

        # Lista wyboru kolumn – uaktualniana po wczytaniu pliku
        tk.Label(plot_options_frame, text="Wybierz kolumny do wykresu:").grid(row=0, column=0, padx=5, sticky="w")
        self.listbox_columns = tk.Listbox(plot_options_frame, selectmode=tk.MULTIPLE, width=30, height=8)
        self.listbox_columns.grid(row=1, column=0, padx=5, pady=5)

        # Pasek przewijania dla listy kolumn
        scrollbar = tk.Scrollbar(plot_options_frame, orient="vertical")
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.listbox_columns.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_columns.yview)

        # Menu wyboru typu wykresu
        tk.Label(plot_options_frame, text="Wybierz typ wykresu:").grid(row=0, column=2, padx=5, sticky="w")
        self.plot_type = tk.StringVar()
        self.plot_type.set("Histogram")  # domyślnie Histogram
        self.option_menu = tk.OptionMenu(plot_options_frame, self.plot_type, "Histogram", "Linia")
        self.option_menu.grid(row=1, column=2, padx=5, pady=5)

        # Przycisk generowania wykresu z wybranych kolumn
        self.btn_plot_selected = tk.Button(plot_options_frame, text="Wykres wybranych kolumn", command=self.plot_selected_data)
        self.btn_plot_selected.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Przycisk zapisu wykresu
        self.btn_save_chart = tk.Button(plot_options_frame, text="Zapisz wykres", command=self.save_chart)
        self.btn_save_chart.grid(row=2, column=2, padx=5, pady=5)

        # Ramka do wyświetlania wykresu
        self.plot_frame = tk.Frame(root)
        self.plot_frame.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            try:
                sep = self.entry_separator.get()
                comment = self.entry_comment.get()
                encoding = self.entry_encoding.get()
                self.df = pd.read_csv(file_path, sep=sep, comment=comment, encoding=encoding)
                messagebox.showinfo("Sukces", "Plik CSV wczytany poprawnie.")
                self.text_stats.delete(1.0, tk.END)
                self.text_stats.insert(tk.END, "Plik wczytany. Możesz teraz przeprowadzić analizę.\n")
                self.update_columns_list()
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd wczytywania pliku: {e}")

    def update_columns_list(self):
        # Uaktualnia listbox nazwami kolumn wczytanego pliku
        self.listbox_columns.delete(0, tk.END)
        if self.df is not None:
            for col in self.df.columns:
                self.listbox_columns.insert(tk.END, col)

    def analyze_data(self):
        if self.df is None:
            messagebox.showerror("Błąd", "Najpierw wczytaj plik CSV.")
            return
        try:
            stats = self.df.describe(include="all").to_string()
            info = f"Liczba wierszy: {self.df.shape[0]}\nLiczba kolumn: {self.df.shape[1]}\n"
            missing = "Brakujące wartości:\n" + self.df.isnull().sum().to_string()
            full_stats = stats + "\n\n" + info + "\n" + missing
            self.text_stats.delete(1.0, tk.END)
            self.text_stats.insert(tk.END, full_stats)
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd analizy danych: {e}")

    def plot_selected_data(self):
        if self.df is None:
            messagebox.showerror("Błąd", "Najpierw wczytaj plik CSV.")
            return

        # Pobranie wybranych kolumn z listy
        selected_indices = self.listbox_columns.curselection()
        if not selected_indices:
            messagebox.showerror("Błąd", "Wybierz przynajmniej jedną kolumnę do wykresu.")
            return
        selected_columns = [self.listbox_columns.get(i) for i in selected_indices]
        plot_type = self.plot_type.get()

        try:
            # Usunięcie poprzedniego wykresu
            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            # Utworzenie nowej figury
            self.fig = plt.Figure(figsize=(6, 4))
            ax = self.fig.add_subplot(111)

            if plot_type == "Histogram":
                for col in selected_columns:
                    # Wykres histogramu tylko dla kolumn numerycznych
                    if pd.api.types.is_numeric_dtype(self.df[col]):
                        self.df[col].plot(kind="hist", ax=ax, alpha=0.5, label=col)
                    else:
                        messagebox.showwarning("Ostrzeżenie", f"Kolumna '{col}' nie jest numeryczna i zostanie pominięta.")
                ax.set_title("Histogram wybranych kolumn")
            elif plot_type == "Linia":
                for col in selected_columns:
                    if pd.api.types.is_numeric_dtype(self.df[col]):
                        self.df[col].plot(kind="line", ax=ax, label=col)
                    else:
                        messagebox.showwarning("Ostrzeżenie", f"Kolumna '{col}' nie jest numeryczna i zostanie pominięta.")
                ax.set_title("Wykres liniowy wybranych kolumn")
            ax.legend()

            self.fig.tight_layout()
            canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd generowania wykresu: {e}")

    def save_csv(self):
        if self.df is None:
            messagebox.showerror("Błąd", "Brak danych do zapisu.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("All files", "*.*")])
        if file_path:
            try:
                if file_path.endswith(".xlsx"):
                    self.df.to_excel(file_path, index=False)
                else:
                    self.df.to_csv(file_path, index=False)
                messagebox.showinfo("Sukces", "Dane zapisane poprawnie.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd zapisu danych: {e}")

    def save_stats(self):
        stats = self.text_stats.get(1.0, tk.END)
        if not stats.strip():
            messagebox.showerror("Błąd", "Brak wygenerowanych statystyk do zapisu.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Pliki tekstowe", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(stats)
                messagebox.showinfo("Sukces", "Statystyki zapisane poprawnie.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd zapisu statystyk: {e}")

    def save_chart(self):
        if self.fig is None:
            messagebox.showerror("Błąd", "Brak wykresu do zapisu.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            try:
                self.fig.savefig(file_path)
                messagebox.showinfo("Sukces", "Wykres zapisany poprawnie.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Błąd zapisu wykresu: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnalyzerApp(root)
    root.mainloop()
