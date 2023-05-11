import os
from datetime import datetime


# 1 Доработать декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log'
# дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Функция test_1 в коде ниже также должна отработать без ошибок.

def logger(old_function):
    def new_function(*args, **kwargs):
        path = 'main.log'
        with open(path, 'a') as log_file:
            log_file.write(
                f'{datetime.now()} - функция {old_function.__name__} вызвана с аргументами {args}, {kwargs}\n')
            result = old_function(*args, **kwargs)
            log_file.write(f'{datetime.now()} - функция {old_function.__name__} возвращает {result}\n')
        return result

    return new_function


def test_1():
    path = 'main.log'

    # if os.path.exists(path):
    #     os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    result1 = hello_world()
    result2 = summator(2, 2)
    result3 = div(6, 2)

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()


if __name__ == '__main__':
    test_1()


# 2 Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает
# в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать
# без ошибок.

def logger2(path):
    def __logger2(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, "a") as log_file:
                log_file.write(f"{datetime.now()} - {old_function.__name__} - {args} - {kwargs} - {result}\n")

            return result

        return new_function

    return __logger2


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        # if os.path.exists(path):
        #     os.remove(path)

        @logger2(path)
        def hello_world():
            return 'Hello World'

        @logger2(path)
        def summator(a, b=0):
            return a + b

        @logger2(path)
        def div(a, b):
            return a / b

        result1 = hello_world()
        result2 = summator(2, 2)
        result3 = div(6, 2)

        summator(4.3, b=2.2)
        summator(a=0, b=0)


if __name__ == '__main__':
    test_2()


# 3 Применить написанный логгер к приложению из любого предыдущего д/з.

# ДЗ по итераторам (п.1)
class FlatIterator:
    def __init__(self, list_of_lists):
        self.flat_list = []
        self.flatten(list_of_lists)

    def flatten(self, lst):
        for item in lst:
            if type(item) == list:
                self.flatten(item)
            else:
                self.flat_list.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


def test_3():
    @logger2('log_iter.log')
    def list_of_lists(lol):
        return FlatIterator(lol).flat_list

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    flat_list = list_of_lists(list_of_lists_1)


if __name__ == '__main__':
    test_3()
