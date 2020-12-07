"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""

import random


def random_generator(start, finish):
    generated_list = []
    generated_dict = {}
    for i in range(10):
        random_number = int((finish - start) * random.random() + start)
        generated_list.append(random_number)
        generated_dict[f'elem_{format(random_number)}'] = random_number

    return (generated_list, generated_dict)

print(random_generator(5,15))
