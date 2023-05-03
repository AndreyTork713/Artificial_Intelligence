# Модуль Neuron
import numpy as np

# функция активации
def onestep(x):
    b = 5
    if x >= b:
        return 1
    else:
        return 0

# Создание класса "Нейрон"

class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):             # Сумматор
        s = np.dot(self.w, x)     # Суммируем входы
        return onestep(s)                # функция активации


Xi = np.array([0, 0, 1, 1])           # Задание значений входам
Wi = np.array([5, 4, 3, 1])           # Веса входных сенсоров
n = Neuron(Wi)                        # Создание объекта класса Neuron
print('Y = ', n.y(Xi))               # Обращение к нейрону

