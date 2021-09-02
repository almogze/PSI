import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PSI experiment")
        self.setWindowIcon(QtGui.QIcon("Atom-Chip.jpg"))


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
