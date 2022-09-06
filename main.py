import sys
from settings import Settings
from window import SettingsWindow
from PyQt5.QtWidgets import QApplication

from numpy.random import randint

app = QApplication([])
# Класс настроек, будет передан в окно 'SettingsWindow'
colors = randint(0, 256, size=(8,3)) # Случайные цвета каналов
settings = Settings(power_line_filter=True, highpass_filter=True, gain=1,
                    mode='normal', sampling_rate=250, channel_colors=colors,
                    black_theme=True)

window = SettingsWindow(settings)

window.show()
sys.exit(app.exec())