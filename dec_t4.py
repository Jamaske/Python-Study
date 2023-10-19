'''
Напишите декоратор retry:

декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции.
При сбое декоратор должен подождать и повторить попытку выполнения функции.
При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
Если у декоратора заканчиваются попытки, он сдается и возвращает исключение
'''


def retry(func):
    from time import sleep
    def wrapper(*args, **kwargs):
        delay = 1;
        while True:
            status = func(args, kwargs)
            if status:
                break
            sleep(delay)
            delay *= 2
    return wrapper


@retry
def test_subject(retrus):
    for i in range(retrus - 1):
        yield False

    yield True

test_subject(5)