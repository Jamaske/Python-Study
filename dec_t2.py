import functools
import random

from typing import List

# Модифицируйте код декоратора prime_filter
def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        given_num = func(*args, **kwargs)
        simple_subset = []
        for i in given_num:
            j = 2
            while j*j <= i:
                if i % j == 0:
                    break
                j += 1
            else:
                simple_subset.append(i)
        return simple_subset
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

# вывод для примера
print(numbers(from_num=2, to_num=20)) 
