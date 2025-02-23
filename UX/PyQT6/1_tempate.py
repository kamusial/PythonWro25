from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
import sys

app = QApplication(sys.argv)   # tworzenie aplikacji
window = QDialog()             # tworznie okna QDialog

window.show()                  # uruchimienie okna
app.exec()                     # uruchomienie aplikacji
