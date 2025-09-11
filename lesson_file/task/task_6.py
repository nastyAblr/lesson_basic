"""
Напишите программу для чтения последних n строк файла.

"""
from collections import deque

n = 2
with open('D:/dok3.txt', 'r', encoding=None) as my_file3:
    res = deque(my_file3, maxlen=n)
print(''.join(res[-n]))


