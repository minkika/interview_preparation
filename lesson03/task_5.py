"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""

import re

with open('new_file_task4.txt', encoding='utf-8') as source_file:
    with open('new_file_task5.txt', 'w', encoding='utf-8') as result_file:
        for line in source_file:
            text = re.findall(r'[a-z]+', line)[0]
            result_file.writelines(re.sub(r'\d+', text, line))
