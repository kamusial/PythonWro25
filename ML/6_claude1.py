import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os


class FileAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizator Plików")
        self.root.geometry("800x600")
        self.df = None

        # Zmienne do przechowywania wyborów użytkownika
        self.input_format = tk.StringVar(value="csv")
        self.output_format = tk.StringVar(value="csv")
        self.separator = tk.StringVar(value=",")
        self.encoding = tk.StringVar(value="utf-8")

        self.create_widgets()

    def create_widgets(self):
        # Frame główny
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Sekcja wejściowa
        input_frame = ttk.LabelFrame(main_frame, text="Wczytywanie pliku", padding="5")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(input_frame, text="Format wejściowy:").grid(row=0, column=0, padx=5)
        input_format_combo = ttk.Combobox(input_frame, textvariable=self.input_format)
        input_format_combo['values'] = ('csv', 'excel', 'txt')
        input_format_combo.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Separator:").grid(row=1, column=0, padx=5)
        separator_entry = ttk.Entry(input_frame, textvariable=self.separator)
        separator_entry.grid(row=1, column=1, padx=5)

        ttk.Label(input_frame, text="Kodowanie:").grid(row=2, column=0, padx=5)
        encoding_entry = ttk.Entry(input_frame, textvariable=self.encoding)
        encoding_entry.grid(row=2, column=1, padx=5)

        ttk.Button(input_frame, text="Wybierz plik", command=self.load_file).grid(row=3, column=0, columnspan=2, pady=5)

        # Sekcja analizy
        analysis_frame = ttk.LabelFrame(main_frame, text="Analiza danych", padding="5")
        analysis_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        self.analysis_text = tk.Text(analysis_frame, height=10, width=70)
        self.analysis_text.grid(row=0, column=0, padx=5, pady=5)

        # Sekcja wyjściowa
        output_frame = ttk.LabelFrame(main_frame, text="Zapisywanie pliku", padding="5")
        output_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(output_frame, text="Format wyjściowy:").grid(row=0, column=0, padx=5)
        output_format_combo = ttk.Combobox(output_frame, textvariable=self.output_format)
        output_format_combo['values'] = ('csv', 'excel', 'txt')
        output_format_combo.grid(row=0, column=1, padx=5)

        ttk.Button(output_frame, text="Zapisz plik", command=self.save_file).grid(row=1, column=0, columnspan=2, pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx;*.xls"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            if self.input_format.get() == 'csv':
                self.df = pd.read_csv(file_path, sep=self.separator.get(), encoding=self.encoding.get())
            elif self.input_format.get() == 'excel':
                self.df = pd.read_excel(file_path)
            else:  # txt
                self.df = pd.read_csv(file_path, sep=self.separator.get(), encoding=self.encoding.get())

            self.analyze_data()

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wczytać pliku: {str(e)}")

    def analyze_data(self):
        if self.df is None:
            return

        analysis_results = []

        # Sprawdzanie pustych wartości
        null_counts = self.df.isnull().sum()
        if null_counts.any():
            analysis_results.append("Znaleziono puste wartości:")
            for column, count in null_counts[null_counts > 0].items():
                analysis_results.append(f"- Kolumna '{column}': {count} pustych wartości")

        # Sprawdzanie zerowych wartości w kolumnach numerycznych
        numeric_columns = self.df.select_dtypes(include=['int64', 'float64']).columns
        for column in numeric_columns:
            zero_count = (self.df[column] == 0).sum()
            if zero_count > 0:
                analysis_results.append(f"Kolumna '{column}': {zero_count} zerowych wartości")

        # Podstawowe statystyki
        analysis_results.append("\nPodstawowe statystyki:")
        analysis_results.append(f"Liczba wierszy: {len(self.df)}")
        analysis_results.append(f"Liczba kolumn: {len(self.df.columns)}")

        # Wyświetlanie wyników
        self.analysis_text.delete(1.0, tk.END)
        self.analysis_text.insert(tk.END, "\n".join(analysis_results))

    def save_file(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik!")
            return

        file_types = []
        if self.output_format.get() == 'csv':
            file_types = [("CSV files", "*.csv")]
            default_ext = ".csv"
        elif self.output_format.get() == 'excel':
            file_types = [("Excel files", "*.xlsx")]
            default_ext = ".xlsx"
        else:  # txt
            file_types = [("Text files", "*.txt")]
            default_ext = ".txt"

        file_path = filedialog.asksaveasfilename(
            defaultextension=default_ext,
            filetypes=file_types
        )

        if not file_path:
            return

        try:
            if self.output_format.get() == 'csv':
                self.df.to_csv(file_path, sep=self.separator.get(), encoding=self.encoding.get(), index=False)
            elif self.output_format.get() == 'excel':
                self.df.to_excel(file_path, index=False)
            else:  # txt
                self.df.to_csv(file_path, sep=self.separator.get(), encoding=self.encoding.get(), index=False)

            messagebox.showinfo("Sukces", "Plik został zapisany pomyślnie!")

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileAnalyzerApp(root)
    root.mainloop()