import functools
import random

from typing import List

# Модифицируйте код декоратора reverse_string
def reverse_string(func):
    #func == get_univerity_mane or any other decorated function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if type(ret) != str:
            return None
        else:
            return ret[::-1]
    # re-assigns wrapper function to func (after this neme get_university_name will point to wrapper function)
    return wrapper


@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() :
    return 1957

# вывод для примера
print(
    get_university_name(),
    get_university_founding_year(),
    sep="\n"
)
