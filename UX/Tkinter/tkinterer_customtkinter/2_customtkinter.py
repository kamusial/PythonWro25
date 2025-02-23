import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import json
import plotly.graph_objects as go
import webbrowser


class AdvancedCustomTkinterApp:
    def __init__(self):
        # Konfiguracja głównego okna
        self.app = ctk.CTk()
        self.app.title("Zaawansowana Aplikacja CustomTkinter")
        self.app.geometry("1000x800")

        # Ustawienia wyglądu
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        # Tworzenie głównego układu
        self.create_sidebar()
        self.create_main_frame()

        # Inicjalizacja zmiennych
        self.current_frame = None
        self.show_dashboard()

    def create_sidebar(self):
        # Panel boczny
        self.sidebar = ctk.CTkFrame(self.app, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=0, pady=0)
        self.sidebar.pack_propagate(False)

        # Logo i tytuł
        self.logo_label = ctk.CTkLabel(self.sidebar, text="CustomTkinter\nDemo App",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)

        # Przyciski nawigacyjne
        self.nav_buttons = []
        nav_items = [
            ("Dashboard", self.show_dashboard),
            ("Formularz", self.show_form),
            ("Wykresy", self.show_charts),
            ("Ustawienia", self.show_settings)
        ]

        for text, command in nav_items:
            btn = ctk.CTkButton(self.sidebar, text=text, command=command,
                                fg_color="transparent", text_color=("gray10", "gray90"))
            btn.pack(pady=5)
            self.nav_buttons.append(btn)

        # Przełącznik motywu
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.sidebar,
            values=["System", "Light", "Dark"],
            command=self.change_appearance_mode)
        self.appearance_mode_menu.pack(pady=20)

        # Suwak postępu
        self.sidebar_progress = ctk.CTkProgressBar(self.sidebar)
        self.sidebar_progress.pack(pady=20)
        self.sidebar_progress.set(0.7)

    def create_main_frame(self):
        # Główny kontener na zawartość
        self.main_frame = ctk.CTkFrame(self.app)
        self.main_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    def show_dashboard(self):
        self.clear_main_frame()

        # Nagłówek
        header = ctk.CTkLabel(self.main_frame,
                              text="Dashboard",
                              font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=20)

        # Karty statystyk
        stats_frame = ctk.CTkFrame(self.main_frame)
        stats_frame.pack(fill="x", pady=20)

        for i, (title, value) in enumerate([
            ("Użytkownicy", "1,234"),
            ("Aktywne sesje", "56"),
            ("Powiadomienia", "7")
        ]):
            card = ctk.CTkFrame(stats_frame)
            card.grid(row=0, column=i, padx=10, sticky="ew")
            stats_frame.grid_columnconfigure(i, weight=1)

            ctk.CTkLabel(card, text=title,
                         font=ctk.CTkFont(size=14)).pack(pady=5)
            ctk.CTkLabel(card, text=value,
                         font=ctk.CTkFont(size=20, weight="bold")).pack(pady=5)

        # Wykres przykładowy
        chart_frame = ctk.CTkFrame(self.main_frame)
        chart_frame.pack(fill="both", expand=True, pady=20)

        # Lista ostatnich aktywności
        activities_frame = ctk.CTkFrame(self.main_frame)
        activities_frame.pack(fill="x", pady=20)

        ctk.CTkLabel(activities_frame, text="Ostatnie aktywności",
                     font=ctk.CTkFont(weight="bold")).pack(pady=10)

        for activity in ["Nowe logowanie", "Aktualizacja profilu", "Nowa wiadomość"]:
            activity_row = ctk.CTkFrame(activities_frame)
            activity_row.pack(fill="x", pady=2)
            ctk.CTkLabel(activity_row, text=activity).pack(side="left", padx=10)
            ctk.CTkLabel(activity_row, text=datetime.now().strftime("%H:%M")).pack(side="right", padx=10)

    def show_form(self):
        self.clear_main_frame()

        # Nagłówek formularza
        header = ctk.CTkLabel(self.main_frame,
                              text="Formularz rejestracyjny",
                              font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=20)

        # Kontener formularza
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Pola formularza
        fields = [
            ("Imię:", ctk.CTkEntry),
            ("Email:", ctk.CTkEntry),
            ("Hasło:", ctk.CTkEntry),
            ("Opis:", ctk.CTkTextbox),
            ("Wiek:", ctk.CTkSlider),
            ("Newsletter:", ctk.CTkCheckBox),
            ("Płeć:", ctk.CTkSegmentedButton)
        ]

        self.form_widgets = {}

        for i, (label_text, widget_class) in enumerate(fields):
            label = ctk.CTkLabel(form_frame, text=label_text)
            label.grid(row=i, column=0, padx=20, pady=10, sticky="e")

            if widget_class == ctk.CTkSegmentedButton:
                widget = widget_class(form_frame, values=["Mężczyzna", "Kobieta", "Inne"])
            elif widget_class == ctk.CTkSlider:
                widget = widget_class(form_frame, from_=0, to=100)
            elif widget_class == ctk.CTkTextbox:
                widget = widget_class(form_frame, height=100)
            elif widget_class == ctk.CTkEntry and "Hasło" in label_text:
                widget = widget_class(form_frame, show="*")
            else:
                widget = widget_class(form_frame)

            widget.grid(row=i, column=1, padx=20, pady=10, sticky="ew")
            self.form_widgets[label_text] = widget

        # Przyciski formularza
        button_frame = ctk.CTkFrame(form_frame)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        ctk.CTkButton(button_frame, text="Zapisz",
                      command=self.save_form).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Wyczyść",
                      command=self.clear_form).pack(side="left", padx=10)

    def show_charts(self):
        self.clear_main_frame()

        # Nagłówek
        header = ctk.CTkLabel(self.main_frame,
                              text="Wykresy i statystyki",
                              font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=20)

        # Ramka kontrolna
        control_frame = ctk.CTkFrame(self.main_frame)
        control_frame.pack(fill="x", pady=20)

        # Wybór typu wykresu
        chart_type = ctk.CTkSegmentedButton(
            control_frame,
            values=["Liniowy", "Słupkowy", "Kołowy"],
            command=self.update_chart
        )
        chart_type.pack(pady=10)

        # Obszar wykresu
        self.chart_frame = ctk.CTkFrame(self.main_frame)
        self.chart_frame.pack(fill="both", expand=True, pady=20)

    def show_settings(self):
        self.clear_main_frame()

        # Nagłówek
        header = ctk.CTkLabel(self.main_frame,
                              text="Ustawienia",
                              font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=20)

        # Kontener ustawień
        settings_frame = ctk.CTkFrame(self.main_frame)
        settings_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Ustawienia wyglądu
        appearance_frame = ctk.CTkFrame(settings_frame)
        appearance_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(appearance_frame, text="Wygląd aplikacji",
                     font=ctk.CTkFont(weight="bold")).pack(pady=10)

        # Suwak skalowania UI
        scale_label = ctk.CTkLabel(appearance_frame, text="Skalowanie UI:")
        scale_label.pack()

        scaling_optionemenu = ctk.CTkOptionMenu(
            appearance_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling
        )
        scaling_optionemenu.pack(pady=10)

        # Ustawienia powiadomień
        notifications_frame = ctk.CTkFrame(settings_frame)
        notifications_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(notifications_frame, text="Powiadomienia",
                     font=ctk.CTkFont(weight="bold")).pack(pady=10)

        notifications_switch = ctk.CTkSwitch(notifications_frame,
                                             text="Włącz powiadomienia")
        notifications_switch.pack(pady=10)

        # Ustawienia dźwięku
        sound_frame = ctk.CTkFrame(settings_frame)
        sound_frame.pack(fill="x", pady=10)

        ctk.CTkLabel(sound_frame, text="Głośność",
                     font=ctk.CTkFont(weight="bold")).pack(pady=10)

        volume_slider = ctk.CTkSlider(sound_frame, from_=0, to=100)
        volume_slider.pack(pady=10)
        volume_slider.set(50)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode.lower())

    def change_scaling(self, new_scaling):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def save_form(self):
        # Przykładowa funkcja zapisu formularza
        data = {}
        for label, widget in self.form_widgets.items():
            if isinstance(widget, ctk.CTkTextbox):
                data[label] = widget.get("0.0", "end")
            elif isinstance(widget, ctk.CTkSlider):
                data[label] = widget.get()
            elif isinstance(widget, ctk.CTkCheckBox):
                data[label] = widget.get()
            elif isinstance(widget, ctk.CTkSegmentedButton):
                data[label] = widget.get()
            else:
                data[label] = widget.get()

        print("Zapisano dane:", data)

    def clear_form(self):
        for widget in self.form_widgets.values():
            if isinstance(widget, ctk.CTkTextbox):
                widget.delete("0.0", "end")
            elif isinstance(widget, ctk.CTkSlider):
                widget.set(0)
            elif isinstance(widget, ctk.CTkCheckBox):
                widget.deselect()
            else:
                widget.delete(0, "end")

    def update_chart(self, chart_type):
        # Przykładowa funkcja aktualizacji wykresu
        print(f"Aktualizacja wykresu na typ: {chart_type}")

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    app = AdvancedCustomTkinterApp()
    app.run()