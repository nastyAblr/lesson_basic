"""
Напишите программу поиска простых чисел.
Ввод и вывод чисел необходимо организовать через файлы.
"""

# with open('D:/dok2.txt', 'r+', encoding='utf-8') as my_file:
    #     for line in my_file:
    #         for token in line.split():
    #             num_file = int(float(token))
    #             print(type(num_file ))
    #             if num_file  % 2 == 0:
    #                 print(my_file.write(f'{num_file } четное число'))
    #             else:
    #                 print(False)
    # print(my_file.closed)


with open('D:/dok2.txt', 'r', encoding='utf-8') as my_file:
    primes = []
    for line in my_file:
        for token in line.split():
            try:
                num_file = int(float(token))
            except ValueError:
                continue

            if num_file <= 1:
                continue
            if num_file == 2:
                primes.append(num_file)
                continue
            if num_file % 2 == 0:
                continue
            i = 3
            is_prime = True
            while i ** 2 <= num_file:
                if num_file % i == 0:
                    is_prime = False
                    break
                i += 2
            if is_prime:
                primes.append(num_file)
print(primes)
with open('D:/dok2.output.txt', 'w', encoding='utf-8') as task_3:
    task_3.write('\n'.join(map(str, primes)))
