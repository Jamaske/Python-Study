import datetime

def generate_dates(day, month, year):
    date = datetime.date(year, month, day)
    while True:
        yield date
        date += datetime.timedelta(days=1)


if __name__ == "__main__":
    for date in generate_dates(1,1,2023):
        if date.year == 2024:
            break
        print(date)