"""
Напишите программу, которая объединяет словари.
"""
dict1 = {1: 2, 1: 3}

dict2 = {4: 5, 3: 12}

dict3 = {**dict1, **dict2}
print(dict3)

"""
Добавьте в словарь {“hello”:”world”} ключ programming language: [python, java, c++].
"""

data_1 = {'hello': 'world', 'programming language': ['python', 'java', 'c++']}

dict3.update(data_1)
print(dict3)
