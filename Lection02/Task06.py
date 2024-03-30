"""
print(0.1 + 0.2)

pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
print(pi)

DEFAULT = 42
num = int(input('Введите уровень или ноль для значения по умолчанию: '))
level = num or DEFAULT
print(level)

name = input('Как вас зовут? ')
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, приветствую')
"""

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())