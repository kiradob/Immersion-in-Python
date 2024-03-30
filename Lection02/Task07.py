txt = 'Книга называется "Война и мир".'


class str(object):
    """
    20
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    ...
    """


text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
print(text)

very_long_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab alias animi assumenda at aut ' \
                 'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \
                 'numquam obcaecati officia officiis porro possimus praesentium quaerat temporibus ullam veniam? '

LIMIT = 120
ATTENTION = 'Внимание!'
21
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) + \
       " до ста лет, но длинна строки не должна превышать "
str(LIMIT) + ' символов.'
print(text)