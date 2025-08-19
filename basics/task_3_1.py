import math

figure = input('Пользователь выбирает фигуру: прямоугольник, треугольник, круг: ').lower()
match figure:
    case 'прямоугольник':
        a = float(input('Введите ширину: '))
        b = float(input('Введите высоту: '))
        s = a * b
        print(f'Площадь прямоугольника - {s}')
    case 'треугольник':
        a = float(input('Введите высоту: '))
        b = float(input('Введите основание: '))
        s = 0.5 * a * b
        print(f'Площадь треугольника - {s}')
    case 'круг':
        r = float(input('Введи радиус: '))
        s = math.pi * r ** 2
        print(f'Площадь круга - {s}')
