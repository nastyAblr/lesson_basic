"""
Напишите программу, которая ищет среди слов
самое длинное.
Ввод и вывод слов необходимо организовать через файлы.
"""
# path = input('D:/dok3.txt')

my_file =  open('D:/dok3.txt', 'r', encoding=None)

length = my_file.readlines()
string = length[0]
string_split = string.split()
print(string_split)
data = []
for i in string_split:
    data.append(len(i))
    word = max(data)
for j in string_split:
    if len(j) == word:
        print(j)
my_file.close()
print(my_file.closed)


