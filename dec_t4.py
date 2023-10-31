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

def loger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} function call')
        ret = func(*args, **kwargs)
        print(f'{func.__name__} function exit')
        return ret
    return wrapper()
@loger
#@retry
def test_subject(returns):
    for i in range(returns - 1):
        yield False
    yield True
    yield False


for i in test_subject(5):
    print(i)

