import random

def main():
    # Обучающая выборка (идеальное изображение цифр от 0 до 9)


    num0 = list('111101101101111')
    num1 = list('001001001001001')
    num2 = list('111001111100111')
    num3 = list('111001111001111')
    num4 = list('101101111001001')
    num5 = list('111100111001111')
    num6 = list('111100111101111')
    num7 = list('111001001001001')
    num8 = list('111101111101111')
    num9 = list('111101111001111')

    # Упаковываем все цифры в единый массив
    nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

    tema = 5 # Какой цифре обучаем
    n_sensor = 15 # количество входных сенсоров

    # Инициализация весов для связей сенсоров с сумматором
    weights = [0 for i in range(n_sensor)] #(Обнуление весов)

    # Функция определяет, является ли полученное изображение числом 5
    def perseptron(Sensor):
        b = 7  # Порог функции активации (может быть любым)
        s = 0  # Начальное значение суммы

        for i in range(n_sensor):  # Цикл сумирования сигналов от сенсоров
            s += int(Sensor[i]) * weights[i]

            if s >= b:
                return True  # Сумма превысила порог
            else:
                return False # Сумма меньше порога

        # НАКАЗАНИЕ
        # Уменьшение значений весов если сеть ошиблась
    def decrease(number):
        for i in range(n_sensor):
            if int(number[i]) == 1:  # Проверяем возбужденный ли вход
                weights[i] -= 1      # Уменьшаем вес на 1

        # ПООЩРЕНИЕ
        # Увеличение значений весов если сеть угадала
    def increase(number):
        for i in range(n_sensor):
            if int(number[i]) == 1:  # Проверяем возбужденный ли вход
                weights[i] += 1      # Увеличиваем вес на 1


    # ТРЕНИРОВКА СЕТИ
    n = 10000 # Кол-во уроков
    for i in range(n):
        j = random.randint(0, 9) # Генерируем случайное число j от 0 до 9
        r = perseptron(nums[j])  # РЕЗУЛЬТАТ ОБРАЩЕНИЯ К СУММАТОРУ (Да или Нет)
        if j != tema:
            if r:
                decrease(nums[j])
        else:
            if not r:
                increase(nums[tema])
    print(weights)
    for item in weights:
        if item >= 1:
            item = 1
        else:
            item = 0
    # Проверка работы программы на обучающей выборке

    print(weights)
    print(f'0 это 5?: {perseptron(num0)}')
    print(f'1 это 5?: {perseptron(num1)}')
    print(f'2 это 5?: {perseptron(num2)}')
    print(f'3 это 5?: {perseptron(num3)}')
    print(f'4 это 5?: {perseptron(num4)}')
    print(f'5 это 5?: {perseptron(num5)}')
    print(f'6 это 5?: {perseptron(num6)}')
    print(f'7 это 5?: {perseptron(num7)}')
    print(f'8 это 5?: {perseptron(num8)}')
    print(f'9 это 5?: {perseptron(num9)}')



if __name__ == '__main__':
    main()