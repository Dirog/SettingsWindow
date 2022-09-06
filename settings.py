import numpy as np
from dataclasses import dataclass

@dataclass
class Settings:
    """ Класс настроек """
    # Filters
    power_line_filter : bool # Настройка '50 Гц'
    highpass_filter : bool # Настройка 'ФВЧ'
    # ADC
    gain : int # Настройка 'усиление'
    mode : str # Настройка 'режим'
    sampling_rate : int # Настройка 'ЧД (Гц)'
    # Interface
    # Массив цветов каналов размером 8х3
    # (8 каналов по 3 числа RGB на цвет (от 0 до 255))
    channel_colors : np.array
    black_theme : bool # Флаг темной темы



