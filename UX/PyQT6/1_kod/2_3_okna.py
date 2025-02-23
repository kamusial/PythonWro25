from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QWidget
import sys

app = QApplication(sys.argv)   # tworzenie aplikacji

window1 = QDialog()   # proste okno z X'em do zamknięcia
window1.setWindowTitle('QDialog')

window2 = QWidget()   # proste okno, z X'em, minimalizacją i pełnym ekranem
window2.setWindowTitle('QWidget')

window3 = QMainWindow()            # okno z większą liczbą funkcij
window3.setWindowTitle('QMainWindow')
window3.statusBar().showMessage('ladownaie danych')
window3.menuBar().addMenu('Opcje').addMenu('Dalej')

window1.show()
window2.show()
window3.show()
app.exec()                     # uruchomienie aplikacji
