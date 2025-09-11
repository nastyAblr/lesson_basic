"""
Напишите словарь, где ключи — frozenset из наборов навыков
(например, {"python", "django"}),
а значения — уровень (beginner/advanced). Проверьте поиск.
"""
key = frozenset({"python", "django"})
value = ('beginner', 'advanced')
my_dict = dict(zip(key, value))

print(my_dict)
