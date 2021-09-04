from PySide6.QtWidgets import QFileDialog


class File:
    def __init__(self):
        self.path = None

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename
        print(self.path)