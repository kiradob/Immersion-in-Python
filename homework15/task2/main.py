# Импортируем необходимые модули: argparse, logging, os, namedtuple, Callable и pytest.

import argparse
import logging
import os
from collections import namedtuple
from typing import Callable


import pytest

# Определяем функцию log_to_file(data: str, file: str = 'task2.log'), которая записывает переданные данные в лог-файл с заданным именем.
def log_to_file(data: str, file: str = 'task2.log') -> None:
    logging.basicConfig(filename=file, encoding='UTF-8', level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    logger.info(data)

# Определяем функцию-декоратор wrap_query, которая оборачивает другую функцию и добавляет запись в лог перед и после вызова этой функции.
def wrap_query(func) -> Callable:
    def wrapper(*args, **kwargs):
        log_to_file(f'[INFO] Query started')
        res = func(*args, **kwargs)
        log_to_file(f'[INFO] Query ended')
        return res

    return wrapper

# Определяем функцию get_dir_contents, которая получает содержимое директории (листинг файлов и папок) и возвращает список объектов DirItem, 
# созданных с помощью namedtuple. Каждый объект содержит информацию о файле или папке (имя, расширение, флаг папки, родительская директория).
@wrap_query
def get_dir_contents(dir_path: str = None) -> list[namedtuple]:
    res = []
    DirItem = namedtuple('DirItem', 'name ext is_dir parent')
    if not dir_path:
        dir_path = os.getcwd()
    for item in os.listdir(dir_path):
        abs_path_w_item = os.path.join(dir_path, item)

        name = item if os.path.isdir(abs_path_w_item) else os.path.splitext(item)[0]
        ext = None if os.path.isdir(abs_path_w_item) else os.path.splitext(item)[1]

        new = DirItem(name=name, ext=ext, is_dir=os.path.isdir(abs_path_w_item), parent=f'{dir_path}')
        log_to_file(str(new))
        res.append(new)

    return res

# Определяем функцию cl_parser, которая парсит аргументы командной строки, принимая путь к директории (по умолчанию текущая директория).
def cl_parser() -> str:
    parser = argparse.ArgumentParser(description='Enter the path to get contents')
    parser.add_argument('-p', '--path', default=f'{os.getcwd()}')
    args = parser.parse_args()

    return f'{args.path}'

# В основном блоке программы выполняется следующее:
# Получен путь к директории из аргументов командной строки.
# Вызывается функция get_dir_contents для получения списка объектов DirItem и записи информации о них в лог.
if __name__ == '__main__':
    path = rf'{cl_parser()}'
    # tuples хранит список объектов 'DirItem' (см. *.log файл)
    tuples = get_dir_contents(path)

# Вызывается тестирование с помощью Pytest.
    pytest.main(['-v'])

 
