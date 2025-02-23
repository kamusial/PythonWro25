from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton
import sys

app = QApplication(sys.argv)   # tworzenie aplikacji

button = QPushButton('Nacisnij')
button.show()

app.exec()                     # uruchomienie aplikacji