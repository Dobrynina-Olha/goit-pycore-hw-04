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