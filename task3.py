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