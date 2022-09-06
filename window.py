from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class SettingsWindow(QtWidgets.QWidget):
    """ Класс окна настроек """
    def __init__(self, settings, parent=None):
        super(SettingsWindow, self).__init__(parent)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle('Настройки')
        self.setFixedSize(400,200)
        label = QtWidgets.QLabel(self)
        label.setText('Настройки')
        # Помочь реализовать
        # ...