from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja pierwsza aplikacja')
        self.setFixedSize(600, 400)
        self.button = QPushButton('przycisk')
        self.button.setCheckable(True)
        self.button.pressed.connect(self.button_pressed)
        self.button.released.connect(self.button_released)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toogle)
        self.setCentralWidget(self.button)

    def button_pressed(self):
        print('Wcisniety')
    def button_released(self):
        print('Puszczony')
    def button_clicked(self):
        print('kliknięty')
    def button_toogle(self, checked):
        print(f'stan przycisku {checked}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()                  # uruchimienie okna
app.exec()                     # uruchomienie aplikacji
