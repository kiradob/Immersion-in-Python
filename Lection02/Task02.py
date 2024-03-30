"""
Неизменяемы                            |  Изменяемые
None                                   |
Числа: int, bool, float, complex       |
Последовательности: str, tuple, bytes  |  Последовательности: list, bytearray
Множества: frozenset                   |  Множества: set
                                       |  Отображения: dict
"""

a = 5
print(a, id(a))
a += 1
print(a, id(a))


# txt = 'Hello world!'
# txt[5] = '_'  # TypeError: 'str' object does not support item assignment


txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))


a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))


# Хеш — это криптографическая функция хеширования, которую обычно
# называют просто хэшем. Хеш-функция представляет собой алгоритм,
# который может преобразовать произвольный массив данных в набор бит
# фиксированной длины

x = 42
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
# print(hash(my_list))  # получим ошибку, т.к. list изменяемый ->: unhashable type: 'list'

my_str = input('Enter any text: ')
print(my_str, type(my_str), id(my_str), hash(my_str))