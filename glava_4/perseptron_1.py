# Искусственный нейрон (персептрон)

def main():

    def perseptron(Sensor):
        b = 7           # Порог функции активации
        s = 0           # Начальное значение суммы

        for i in range(15):         # Цикл сумирования сигналов от сенсоров
            s += int(Sensor[i]) * weights[i]

        if s >= b:
            return True
        else:
            return False

    # ПРОВЕРКА РАБОТЫ ИСКУССТВЕННОГО НЕЙРОНА(ПЕРСЕПТРОНА)

    num1 = list('001001001001001')
    num2 = list('111001111100111')

    weights = [1 for i in range(15)] # Всем весам присваиваю значение 1

    print(num1)
    print(perseptron(num1))
    print()
    print(num2)
    print(perseptron(num2))


if __name__ == '__main__':
    main()