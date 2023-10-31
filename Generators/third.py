import datetime


def generate_dow(day, month, year):
    date = datetime.date(2023, 10, 23)
    day_names = ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
    while True:
        yield day_names[date.weekday()]
        date += datetime.timedelta(days = 1)

    iter = generate_dow(2023,10,26)

if __name__ == "__main__":
    for i in iter:
        print(i)