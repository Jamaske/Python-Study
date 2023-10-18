from random import randint
import

def source():
    yield str(randint(0, 10))

word_counter = {}

for word in source():
    word_counter[word] = word_counter.get()