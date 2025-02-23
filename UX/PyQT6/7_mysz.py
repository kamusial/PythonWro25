from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton, QLabel
import sys
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Moja labelka')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0):
        self.label.setText('ruch')

    def mousePressEvent(self, e):
        print(e)
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("nacisnieto lewy")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('Nacisnieto srodkowy')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('Nacisnieto prawy')




app = QApplication(sys.argv)
window = MainWindow()
window.show()                  # uruchimienie okna
app.exec()                     # uruchomienie aplikacji
