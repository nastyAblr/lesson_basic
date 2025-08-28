"""
Есть словарь, где ключ – это название песни, а значение – это её длительность
Пользователь вводит название песни, чтобы посмотреть длительность её воспроизведения.
"""
dict1 = {
    "Arctic Monkeys - Why'd you only call me when you're high": 2.41,
    "Billie Eilish - when the party's over": 3.16,
    "The Weeknd - Blinding Lights": 3.20,
    "Red Hot Chili Peppers – Californication": 5.29,
    "Eminem - Not Afraid: 4:08, Whitney Houston - I Will Always Love You": 4.31,
    "Coldplay - Viva La Vida": 4.02,
    "Sia – Chandelier": 3.59,
    "Dua Lipa – Physical": 3.13,
    "Lana Del Rey - Summertime Sadness": 4.25,
    "Kendrick Lamar – HUMBLE": 2.57,
}
name = input('Введи  название песни из словаря: ')
print(dict1.get(name))
