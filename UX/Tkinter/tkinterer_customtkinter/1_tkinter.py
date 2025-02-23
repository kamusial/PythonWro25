import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinter.colorchooser import askcolor
import json
from datetime import datetime


class AdvancedTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zaawansowana Aplikacja Tkinter")
        self.root.geometry("800x600")

        # Utworzenie menu głównego
        self.create_menu()

        # Utworzenie notebooka (zakładek)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=5, pady=5)

        # Zakładka 1: Formularz
        self.create_form_tab()

        # Zakładka 2: Rysowanie
        self.create_drawing_tab()

        # Zakładka 3: Notatnik
        self.create_notepad_tab()

        # Pasek statusu
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Inicjalizacja zmiennych
        self.drawing = False
        self.last_x = None
        self.last_y = None
        self.current_color = 'black'

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu Plik
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Plik", menu=file_menu)
        file_menu.add_command(label="Zapisz", command=self.save_data)
        file_menu.add_command(label="Wczytaj", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjście", command=self.root.quit)

        # Menu Pomoc
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        help_menu.add_command(label="O programie", command=self.show_about)

    def create_form_tab(self):
        form_frame = ttk.Frame(self.notebook)
        self.notebook.add(form_frame, text="Formularz")

        # Elementy formularza
        ttk.Label(form_frame, text="Imię:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Wiek:").grid(row=1, column=0, padx=5, pady=5)
        self.age_spinbox = ttk.Spinbox(form_frame, from_=0, to=150)
        self.age_spinbox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Płeć:").grid(row=2, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar()
        ttk.Radiobutton(form_frame, text="Mężczyzna", variable=self.gender_var, value="M").grid(row=2, column=1)
        ttk.Radiobutton(form_frame, text="Kobieta", variable=self.gender_var, value="K").grid(row=2, column=2)

        ttk.Label(form_frame, text="Zainteresowania:").grid(row=3, column=0, padx=5, pady=5)
        self.hobby_vars = []
        hobbies = ["Sport", "Muzyka", "Książki", "Podróże"]
        for i, hobby in enumerate(hobbies):
            var = tk.BooleanVar()
            self.hobby_vars.append(var)
            ttk.Checkbutton(form_frame, text=hobby, variable=var).grid(row=3 + i, column=1)

        ttk.Button(form_frame, text="Zapisz dane", command=self.save_form_data).grid(row=7, column=1, pady=20)

    def create_drawing_tab(self):
        drawing_frame = ttk.Frame(self.notebook)
        self.notebook.add(drawing_frame, text="Rysowanie")

        # Przyciski kontrolne
        control_frame = ttk.Frame(drawing_frame)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Button(control_frame, text="Zmień kolor", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Wyczyść", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)

        # Obszar rysowania
        self.canvas = tk.Canvas(drawing_frame, bg='white')
        self.canvas.pack(expand=True, fill='both', padx=5, pady=5)

        # Bindowanie zdarzeń myszy
        self.canvas.bind('<Button-1>', self.start_drawing)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.stop_drawing)

    def create_notepad_tab(self):
        notepad_frame = ttk.Frame(self.notebook)
        self.notebook.add(notepad_frame, text="Notatnik")

        # Obszar tekstu
        self.text_area = scrolledtext.ScrolledText(notepad_frame, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both', padx=5, pady=5)

        # Przyciski
        button_frame = ttk.Frame(notepad_frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(button_frame, text="Zapisz do pliku", command=self.save_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Wczytaj z pliku", command=self.load_text).pack(side=tk.LEFT, padx=5)

    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.current_color, width=2)
            self.last_x = event.x
            self.last_y = event.y

    def stop_drawing(self, event):
        self.drawing = False

    def choose_color(self):
        color = askcolor(title="Wybierz kolor")[1]
        if color:
            self.current_color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_text(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_area.get('1.0', tk.END))
            self.status_var.set(f"Zapisano tekst do {file_path}")

    def load_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', file.read())
            self.status_var.set(f"Wczytano tekst z {file_path}")

    def save_form_data(self):
        data = {
            "imie": self.name_entry.get(),
            "wiek": self.age_spinbox.get(),
            "plec": self.gender_var.get(),
            "zainteresowania": [var.get() for var in self.hobby_vars],
            "data_zapisu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        file_path = filedialog.asksaveasfilename(defaultextension=".json")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            messagebox.showinfo("Sukces", "Dane zostały zapisane!")

    def save_data(self):
        self.save_form_data()

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki JSON", "*.json")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                self.name_entry.delete(0, tk.END)
                self.name_entry.insert(0, data.get("imie", ""))

                self.age_spinbox.delete(0, tk.END)
                self.age_spinbox.insert(0, data.get("wiek", "0"))

                self.gender_var.set(data.get("plec", ""))

                for var, value in zip(self.hobby_vars, data.get("zainteresowania", [])):
                    var.set(value)

                self.status_var.set(f"Wczytano dane z {file_path}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd podczas wczytywania danych: {str(e)}")

    def show_about(self):
        messagebox.showinfo("O programie",
                            "Zaawansowana aplikacja demonstracyjna Tkinter\n"
                            "Pokazuje różne możliwości biblioteki Tkinter\n"
                            "Wersja 1.0")


if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedTkinterApp(root)
    root.mainloop()