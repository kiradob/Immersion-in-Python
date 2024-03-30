"""

"""
x = int("42")
y = int(3.1415)
z = int("hello", base=30)  # Для base допустимы значения от 2 до 36 (цифры и 20 из 26 букв),
                           # т.е. от двоичной до тридцатишестиричной системы счисления.
print(x, y, z, sep='\n')


import sys
STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP


num = 2 ** 16 - 1
b = bin(num)  # 0b1111111111111111
o = oct(num)  # 0o177777
h = hex(num)  # 0xffff
print(b, o, h)