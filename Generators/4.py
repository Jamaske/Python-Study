from second import generate_dates
from third import generate_dow

def generator(day, month, year):
    iter1 = generate_dates(day, month, year)
    iter2 = generate_dow(day, month, year)
    while True:
        yield next(iter1), next(iter2)

if __name__ == "__main__":
    iter = generator(26,10,2023)
    for i in range(10):
        print(next(iter))