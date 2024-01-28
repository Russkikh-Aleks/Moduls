from datetime import datetime as dt
from application.salary import *
from application.db.people import *


def main():
    print(f'Локальное время: {dt.now()}')
    calculate_salary()
    print(f'Время UTC: {dt.utcnow()}')
    get_employees()
    print(f'Локальное время: {dt.today()}')


if __name__ == '__main__':
    main()
