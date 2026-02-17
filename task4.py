
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

    





