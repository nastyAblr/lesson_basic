"""
Напишите программу для копирования
данных из одного файла в другой.
"""
import shutil

# res_ = shutil.copy2(r'D:/dok.txt', r'D:dok2.txt')
# print(res_)

with open('D:/dok.txt') as m_f1, open('D:/dok2.txt', 'w') as m_f2:
    data = m_f1.read()
    m_f2.write(data)
print(m_f2)


