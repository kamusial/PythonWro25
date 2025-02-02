import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import os


class DataAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Aplikacja Analizy Danych")
        master.geometry("650x500")
        self.data = None

        # --- Ramka wyboru pliku ---
        frame_file = tk.Frame(master)
        frame_file.pack(pady=10)

        tk.Label(frame_file, text="Wybierz plik:").pack(side=tk.LEFT, padx=5)
        self.entry_file = tk.Entry(frame_file, width=50)
        self.entry_file.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_file, text="Przeglądaj", command=self.browse_file).pack(side=tk.LEFT, padx=5)

        # --- Ramka wyboru formatu pliku wejściowego ---
        frame_format = tk.Frame(master)
        frame_format.pack(pady=10)

        tk.Label(frame_format, text="Format pliku wejściowego:").pack(side=tk.LEFT, padx=5)
        self.combo_format = ttk.Combobox(frame_format, values=["csv", "excel", "txt"], state="readonly", width=10)
        self.combo_format.current(0)
        self.combo_format.pack(side=tk.LEFT, padx=5)

        # --- Przycisk analizy ---
        tk.Button(master, text="Analizuj plik", command=self.analyze_file).pack(pady=10)

        # --- Okno tekstowe do wyświetlenia wyników analizy ---
        self.text_result = tk.Text(master, height=10, width=70)
        self.text_result.pack(pady=10)

        # --- Ramka opcji zapisu pliku ---
        frame_save = tk.Frame(master)
        frame_save.pack(pady=10)

        tk.Label(frame_save, text="Format zapisu:").pack(side=tk.LEFT, padx=5)
        self.combo_save_format = ttk.Combobox(frame_save, values=["csv", "excel", "txt"], state="readonly", width=10)
        self.combo_save_format.current(0)
        self.combo_save_format.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_save, text="Zapisz plik", command=self.save_file).pack(side=tk.LEFT, padx=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Wszystkie pliki", "*.*")])
        if file_path:
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, file_path)

    def analyze_file(self):
        file_path = self.entry_file.get()
        file_format = self.combo_format.get()

        if not os.path.exists(file_path):
            messagebox.showerror("Błąd", "Plik nie istnieje!")
            return

        try:
            # Wczytanie danych przy uwzględnieniu formatu
            if file_format == "csv":
                self.data = pd.read_csv(file_path)
            elif file_format == "excel":
                self.data = pd.read_excel(file_path)
            elif file_format == "txt":
                # Przyjmujemy, że plik txt jest oddzielany tabulatorami
                self.data = pd.read_csv(file_path, delimiter="\t")
            else:
                messagebox.showerror("Błąd", "Nieobsługiwany format pliku!")
                return

            wynik = ""

            # Analiza pustych pól
            missing = self.data.isnull().sum().sum()
            wynik += f"Liczba pustych pól: {missing}\n"

            # Analiza zerowych wartości tylko w kolumnach numerycznych
            numeric_cols = self.data.select_dtypes(include=['number']).columns
            zeros_count = (self.data[numeric_cols] == 0).sum().sum()
            wynik += f"Liczba zerowych wartości (kolumny numeryczne): {zeros_count}\n"

            # Analiza wystąpień "tma" (sprawdzamy wszystkie komórki, przyjmujemy porównanie case-insensitive)
            tma_count = self.data.applymap(lambda x: 1 if isinstance(x, str) and x.lower() == 'tma' else 0).sum().sum()
            wynik += f"Liczba wystąpień 'tma': {tma_count}\n"

            # Możesz dodać dodatkową logikę np. sprawdzając czy 'tma' występuje w kolumnach numerycznych
            tma_in_numeric = 0
            for col in numeric_cols:
                tma_in_numeric += self.data[col].apply(
                    lambda x: 1 if isinstance(x, str) and x.lower() == 'tma' else 0).sum()
            wynik += f"'tma' w kolumnach numerycznych: {tma_in_numeric}\n"

            self.text_result.delete("1.0", tk.END)
            self.text_result.insert(tk.END, wynik)

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się przetworzyć pliku:\n{e}")

    def save_file(self):
        if self.data is None:
            messagebox.showerror("Błąd", "Brak danych do zapisu. Najpierw przeanalizuj plik.")
            return

        save_format = self.combo_save_format.get()
        filetypes = []
        if save_format == "csv":
            filetypes = [("CSV files", "*.csv")]
        elif save_format == "excel":
            filetypes = [("Excel files", "*.xlsx")]
        elif save_format == "txt":
            filetypes = [("Text files", "*.txt")]
        else:
            messagebox.showerror("Błąd", "Nieobsługiwany format zapisu!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=filetypes[0][1],
                                                 filetypes=filetypes)
        if not file_path:
            return

        try:
            # Zapis pliku z użyciem odpowiedniej metody
            if save_format == "csv":
                self.data.to_csv(file_path, index=False)
            elif save_format == "excel":
                self.data.to_excel(file_path, index=False)
            elif save_format == "txt":
                self.data.to_csv(file_path, sep="\t", index=False)
            messagebox.showinfo("Sukces", "Plik został zapisany pomyślnie!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
