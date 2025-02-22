import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
from datetime import datetime
import os


class CSVAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Analizator CSV")
        self.geometry("1200x800")

        # Zmienne podstawowe
        self.df = None
        self.separator_var = tk.StringVar(value=',')
        self.encoding_var = tk.StringVar(value='utf-8')
        self.header_var = tk.BooleanVar(value=True)
        self.comment_var = tk.StringVar(value='#')

        # Zmienne dla wykresów
        self.plot_type_var = tk.StringVar(value='wykres słupkowy')
        self.x_column_var = tk.StringVar()
        self.y_column_var = tk.StringVar()
        self.color_column_var = tk.StringVar()
        self.plot_title_var = tk.StringVar(value='')

        self.create_widgets()

    def create_widgets(self):
        # Panel konfiguracji
        config_frame = ttk.LabelFrame(self, text="Konfiguracja wczytywania pliku", padding=10)
        config_frame.pack(fill='x', padx=5, pady=5)

        # Pierwszy wiersz konfiguracji
        config_row1 = ttk.Frame(config_frame)
        config_row1.pack(fill='x', pady=5)

        ttk.Button(config_row1, text="Wybierz plik CSV", command=self.load_file).pack(side='left', padx=5)

        ttk.Label(config_row1, text="Separator:").pack(side='left', padx=5)
        separators = [',', ';', '\t', '|']
        ttk.OptionMenu(config_row1, self.separator_var, separators[0], *separators).pack(side='left', padx=5)

        ttk.Label(config_row1, text="Kodowanie:").pack(side='left', padx=5)
        encodings = ['utf-8', 'ascii', 'iso-8859-1', 'cp1250']
        ttk.OptionMenu(config_row1, self.encoding_var, encodings[0], *encodings).pack(side='left', padx=5)

        # Drugi wiersz konfiguracji
        config_row2 = ttk.Frame(config_frame)
        config_row2.pack(fill='x', pady=5)

        ttk.Label(config_row2, text="Znak komentarza:").pack(side='left', padx=5)
        comments = ['#', '%', ';', '//']
        ttk.OptionMenu(config_row2, self.comment_var, comments[0], *comments).pack(side='left', padx=5)

        ttk.Checkbutton(config_row2, text="Pierwszy wiersz jako nagłówek", variable=self.header_var).pack(side='left',
                                                                                                          padx=5)

        # Panel główny
        main_frame = ttk.PanedWindow(self, orient='horizontal')
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Panel wykresów
        plot_frame = ttk.LabelFrame(main_frame, text="Wykresy", padding=10)
        main_frame.add(plot_frame)

        # Opcje wykresów
        plot_options = ttk.Frame(plot_frame)
        plot_options.pack(fill='x', pady=5)

        # Wybór typu wykresu
        plot_type_frame = ttk.LabelFrame(plot_options, text="Typ wykresu", padding=5)
        plot_type_frame.pack(fill='x', pady=5)

        plot_types = ['wykres słupkowy', 'wykres liniowy', 'inny', 'jeszcze inny']
        ttk.OptionMenu(plot_type_frame, self.plot_type_var, plot_types[0], *plot_types).pack(side='left', padx=5)

        # Opcje danych
        data_frame = ttk.LabelFrame(plot_options, text="Wybór danych", padding=5)
        data_frame.pack(fill='x', pady=5)

        ttk.Label(data_frame, text="Oś X:").pack(side='left', padx=5)
        self.x_column_menu = ttk.OptionMenu(data_frame, self.x_column_var, "")
        self.x_column_menu.pack(side='left', padx=5)

        ttk.Label(data_frame, text="Oś Y:").pack(side='left', padx=5)
        self.y_column_menu = ttk.OptionMenu(data_frame, self.y_column_var, "")
        self.y_column_menu.pack(side='left', padx=5)

        ttk.Label(data_frame, text="Grupowanie:").pack(side='left', padx=5)
        self.color_column_menu = ttk.OptionMenu(data_frame, self.color_column_var, "")
        self.color_column_menu.pack(side='left', padx=5)

        # Tytuł wykresu
        ttk.Label(data_frame, text="Tytuł:").pack(side='left', padx=5)
        ttk.Entry(data_frame, textvariable=self.plot_title_var, width=30).pack(side='left', padx=5)

        # Przyciski akcji
        buttons_frame = ttk.Frame(plot_options)
        buttons_frame.pack(fill='x', pady=5)

        ttk.Button(buttons_frame, text="Generuj wykres", command=self.generate_plot).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="Zapisz wykres", command=self.save_plot).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="Wyczyść", command=self.clear_plot).pack(side='left', padx=5)

        # Miejsce na wykres
        self.plot_container = ttk.Frame(plot_frame)
        self.plot_container.pack(fill='both', expand=True)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            try:
                header = 0 if self.header_var.get() else None

                self.df = pd.read_csv(
                    file_path,
                    sep=self.separator_var.get(),
                    encoding=self.encoding_var.get(),
                    header=header,
                    comment=self.comment_var.get()  # Dodana obsługa komentarzy
                )
                self.update_column_menus()
                messagebox.showinfo("Sukces", "Plik został wczytany pomyślnie!")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku: {str(e)}")

    def update_column_menus(self):
        if self.df is None:
            return

        columns = list(self.df.columns)

        # Aktualizacja menu kolumn
        for menu, var in [(self.x_column_menu, self.x_column_var),
                          (self.y_column_menu, self.y_column_var),
                          (self.color_column_menu, self.color_column_var)]:
            menu['menu'].delete(0, 'end')
            var.set('')

            # Dodaj pustą opcję dla grupowania
            if menu == self.color_column_menu:
                menu['menu'].add_command(label="", command=lambda v="": var.set(v))

            # Dodaj wszystkie kolumny
            for col in columns:
                menu['menu'].add_command(label=col, command=lambda v=col, var=var: var.set(v))

    def generate_plot(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik CSV!")
            return

        if not self.x_column_var.get() or not self.y_column_var.get():
            messagebox.showwarning("Ostrzeżenie", "Wybierz kolumny dla osi X i Y!")
            return

        try:
            # Wyczyść poprzedni wykres
            self.clear_plot()

            # Stwórz nowy wykres
            fig, ax = plt.subplots(figsize=(10, 6))

            if self.plot_type_var.get() == 'wykres słupkowy':
                sns.barplot(data=self.df, x=self.x_column_var.get(), y=self.y_column_var.get(),
                            hue=self.color_column_var.get() or None, ax=ax)
            else:  # wykres liniowy
                sns.lineplot(data=self.df, x=self.x_column_var.get(), y=self.y_column_var.get(),
                             hue=self.color_column_var.get() or None, ax=ax)

            # Ustaw tytuł
            if self.plot_title_var.get():
                ax.set_title(self.plot_title_var.get())

            # Dodaj wykres do interfejsu
            canvas = FigureCanvasTkAgg(fig, master=self.plot_container)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wygenerować wykresu: {str(e)}")

    def clear_plot(self):
        for widget in self.plot_container.winfo_children():
            widget.destroy()
        plt.close('all')

    def save_plot(self):
        if not self.plot_container.winfo_children():
            messagebox.showwarning("Ostrzeżenie", "Najpierw wygeneruj wykres!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )

        if file_path:
            try:
                for widget in self.plot_container.winfo_children():
                    if isinstance(widget, tk.Canvas):
                        widget.figure.savefig(file_path, bbox_inches='tight', dpi=300)
                        messagebox.showinfo("Sukces", "Wykres został zapisany!")
                        return
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać wykresu: {str(e)}")


if __name__ == "__main__":
    app = CSVAnalyzer()
    app.mainloop()