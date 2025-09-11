"""
Создайте цикл while,
где пользователь вводит числа,
пока сумма (с моржовой операцией)
не превысит 100.
"""

sum_ = 0
while (s := input('Введи число: ')) != '':
    try:
        a = int(s)
    except ValueError:
        print('Введите целое число или пустую строку для выхода.')
        continue
    if sum_ > 100:
        break
    sum_ += a
    print(sum_)

