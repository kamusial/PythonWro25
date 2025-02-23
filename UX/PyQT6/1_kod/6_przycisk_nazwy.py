from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton
import sys
from random import choice
from PyQt6.QtGui import QIcon
from time import sleep

window_titles = ['nie ma pieska', 'nie ma pieska', 'Merito', 'Merito', 'piesek', 'piesek',
                 'kantyna', 'kantyna', 'BLAD!']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setWindowTitle('Psia aplikacja')
        self.button = QPushButton('przycisk')
        # self.setGeometry(100, 100, 300, 300)
        # self.button.setIcon('icon.png')
        self.button.pressed.connect(self.button_clicked)
        self.setCentralWidget(self.button)
        self.windowTitleChanged.connect(self.wrong_title)

    def button_clicked(self):
        print('Kliknięty')
        current_title = choice(window_titles)
        print(f'nowy tytuł to: {current_title}')
        self.setWindowTitle(current_title)

    def wrong_title(self, tytul_okna):
        print(f'Tytuł zmieniono na {tytul_okna}')
        if tytul_okna == 'BLAD!':
            self.button.setText('Nieaktywny')
            self.button.setDisabled(True)
            sleep(1)
            # self.button.setDisabled(False)
            # self.button.setEnabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()                  # uruchimienie okna
app.exec()                     # uruchomienie aplikacji
