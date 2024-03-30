a = 5
print(type(a), id(a))  # <class 'int'> 140717222720424
a = "hello world"
print(type(a), id(a))  # <class 'str'> 2183450283760
a = 42.0 * 3.141592 / 2.71828
print(type(a), id(a))  # <class 'float'> 2183452067120


data = 42
print(isinstance(data, int))  # True
data = True
print(isinstance(data, int))  # True
data = 3.14
print(isinstance(data, (int, float, complex)))  # True
print(isinstance(data, (int | float | complex)))  # True


num = 2 + 2 * 2
digit = 36 / 6
print(num)  # 6
print(digit)  # 6.0
print(num == digit)  # True
print(num is digit)  # False