name = 'Alex'
age = None

a = 42
print(id(a))
a = 'Hello!'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, 'text', sep=' | ', end='#')
print('second line of text')

res = input('Type in your text: ')
print('You\'ve printed: ', res)

age = int(input('What\'s your age? '))
print(type(age))