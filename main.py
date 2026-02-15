# Завдання 1

from datetime import datetime


def get_days_from_today(date: str) -> int | ValueError:
    """Ф-я розраховує к-сть днів між date та поточною датою

    Args:
        date (str): Дата у форматі "YYYY-MM-DD"

    Returns:
        int: К-сть днів між date та поточною датою
    """
    try:
        current_date = datetime.now().date()
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        return (target_date - current_date).days
    except ValueError:
        raise ValueError(f"Неправильний формат дати - {date}. Використовуйте 'YYYY-MM-DD'")


if __name__ == "__main__":
    print(get_days_from_today("2026-07-01"))



# Завдання 2

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Ф-я, яка генерує набір випадкових унікальних чисел для лотереї

    Args:
        min (int): Мінімальне значення діапазону
        max (int): Максимальне значення діапазону
        quantity (int): Кількість унікальних чисел для генерації

    Returns:
        list: Список унікальних випадкових чисел
    """
    if (min < 1) or (max > 1000) or (quantity < 1) or (quantity > (max - min + 1)):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


if __name__ == "__main__":
    print(get_numbers_ticket(1, 100, 5))


# Завдання 3

import re


def normalize_phone(phone_number: str) -> str:
    """Ф-я, що нормалізує тел. номери до стандартного формату

    Args:
        phone_number (str): Тел. номер у будь-якому форматі

    Returns:
        str: Тел. номер у форматі "+380XXXXXXXXX"
    """
    cleaned = re.sub(r"[^0-9+]", "", phone_number)
    if cleaned.startswith("+380"):
        return cleaned
    elif cleaned.startswith("+"):
        return f"+380{cleaned[1:]}"
    elif cleaned.startswith("380"):
        return f"+{cleaned}"
    elif cleaned.startswith("0"):
        return f"+38{cleaned}"


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    for phone in raw_numbers:
        print(normalize_phone(phone))


# Завдання 4

from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """Ф-я, яка повертає список користувачів з найближчими днями народження

    Args:
        users (list[dict]): Список користувачів, кожен з яких є словником з ключами "name" та "birthday"

    Returns:
        list[dict]: Список користувачів з найближчими днями народження
    """
    current_date = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()

        # 29 лютого обробляється як 28 лютого для невисокосних років
        try:
            next_birthday = birthday.replace(year=current_date.year)
        except ValueError:
            # Handle February 29 for non-leap years
            next_birthday = birthday.replace(year=current_date.year, day=28)

        if next_birthday < current_date:
            next_birthday = next_birthday.replace(year=current_date.year + 1)

        days_until_birthday = (next_birthday - current_date).days
        if days_until_birthday <= 7:
            if next_birthday.weekday() == 5:  # Saturday
                next_birthday += timedelta(days=2)
            elif next_birthday.weekday() == 6:  # Sunday
                next_birthday += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y-%m-%d")
            })
    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Alice", "birthday": "1990-02-13"},
        {"name": "Bob", "birthday": "1985-02-14"},
        {"name": "Charlie", "birthday": "1992-02-15"},
    ]
    print(get_upcoming_birthdays(users))

    





