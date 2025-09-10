"""
Напишите программу для подсчета частоты слов в файле.
"""
import re
import string

frequency = {}
my_file = open('D:/dok.txt', 'r')
text_string = my_file.read().lower()
match_pattern = re.findall(r'\b[а-я]{1,15}\b', text_string)
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words]) # решение взяла в интернете

my_file.close()
print(my_file.closed)