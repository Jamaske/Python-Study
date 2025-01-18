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
        delay = 1
        for i in range(4):
            status = func(*args, **kwargs)
            if status:
                break
            sleep(delay)
            delay *= 2
        raise Exception('Out of retries')
    return wrapper

def loger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} function call')
        ret = func(*args, **kwargs)
        print(f'{func.__name__} function exit')
        return ret
    return wrapper

@retry
@loger
def test_subject(returns):
    return False


test_subject(5)

