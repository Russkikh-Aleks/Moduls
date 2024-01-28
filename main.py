from datetime import datetime as dt
from application.salary import calculate_salary
import application.db.people as people


def main():
    print(f'Локальное время: {dt.now()}')
    calculate_salary()
    print(f'Время UTC: {dt.utcnow()}')
    people.get_employees()
    print(f'Локальное время: {dt.today()}')


if __name__ == '__main__':
    main()
