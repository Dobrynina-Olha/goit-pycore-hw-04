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
 
    print("CHECK_RUN")
