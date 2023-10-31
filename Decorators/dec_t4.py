'''
Напишите декоратор retry:

декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции.
При сбое декоратор должен подождать и повторить попытку выполнения функции.
При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
Если у декоратора заканчиваются попытки, он сдается и возвращает исключение
'''

from time import sleep
import asyncio
def retry(func):
    from time import sleep
    def wrapper(*args, **kwargs):
        delay = 1
        while True:
            status = func(*args, **kwargs)
            print(delay)
            if status:
                break
            delay *= 2
    return wrapper



@retry
def false_func():
    return False



def test_subject(retrys):
    for i in range(retrys - 1):
        yield False

    yield True

print(false_func())


def f(n):
    if n<2: return 1
    else: return f(n-1) + f(n-2)


