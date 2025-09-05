"""
Есть промежуток чисел от 1 до 100.
Нужно вывести все чётные числа.
"""
n = 100
i = 1
while i < 100:
    if i % 2 == 0:
        print(i)
    i = i + 1

"""
Пользователь вводит числа в список. 
Нужно найти сумму этих чисел.
"""

nums = input('Введи список чисел: ')

list_num = []
for x in nums.split():
    list_num.append(int(x))

print(sum(list_num))

"""
Вывести все совершенные числа в диапазоне от 1 до 1000000.
"""
p = 1
while p < 1000000:
    if p == 10:
        break
    a = (2 ** (p - 1) * (2 ** p - 1))

    print(p, a)
    p = p + 1

"""
Найти максимальное и минимальное число в списке, 
не используя функции max() и min().
"""
list_1 = [1, 2, 3, 8, 6]

max_value = list_1[0]
min_value = list_1[0]
for i in range(1, len(list_1)):
    if list_1[i] > max_value:
        max_value = list_1[i]
    if list_1[i] < min_value:
        min_value = list_1[i]
print(max_value, min_value)

"""
Выведите первых 100 чисел из ряда Фибоначчи.
"""
fib1, fib2, fib3 = 0, 0, 1
while fib3 < 100:
    print(fib3)
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2

"""
Посчитать и вывести на экран сумму всех цифр в числе.
"""
str_num = input('Введи число: ')
res = 0
for x in num:
    res += int(x)
print(res)

nums = [int(float(s)) for s in str_num]
print(sum(nums))

"""
Посчитать и вывести словарь, в котором хранится количество положительных, 
отрицательных чисел и нулей в пользовательском списке. 
Вид словаря {"положительных": кол-во, "отрицательных": кол-во,
 "нулей": кол-во}.
"""

data = input('Введи числа положительные, отрицательные, нули: ')
nums = [int(float(x)) for x in data.split()]
positive = sum(True for x in nums if x > 0)
negative = sum(True for x in nums if x < 0)
zeros = sum(True for x in nums if x == 0)

result = {'положительные': positive, 'отрицательные': negative, 'нули': zeros}
print(result)

"""
Вывести на экран таблицу умножения числа n на промежуток от 2 до 10
"""
n_ = int(float(input('Введи число: ')))
table = [f" {i} * {j} = {i * j}"
         for i in range(1, n_ + 1)
         for j in range(2, 11)]
print(table)

"""
Найти все числа, которые делятся нацело на 5 и 7 в пользовательском списке. 
Требуется посчитать сумму таких чисел и вывести ее на экран.
"""
s = input('Введите числа через пробел:  ')
nums = []
for x in s.split():
    val = int((x))
    nums.append(val)
divisible = []
for i in nums:
    if i % 5 == 0 and i % 7 == 0:
        divisible.append(i)
res = sum(divisible)
print(res)
