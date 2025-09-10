"""
Напишите программу, чтобы оценить, закрыт файл или нет.
"""

my_file = open('D:/dok.txt', 'a+', encoding=None)
my_file.write('Я живу в городе Солигорск')

print(my_file)
my_file.close()
print(my_file.closed)



