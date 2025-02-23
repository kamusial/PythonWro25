from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
window = MainWindow()
window.show()                  # uruchimienie okna
app.exec()                     # uruchomienie aplikacji
