"""Модуль для маскировки банковских данных."""


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Отображает первые 6 и последние 4 цифры, остальные заменяет
    звёздочками. Номер разбивается на блоки по 4 цифры.

    Args:
        card_number: Номер карты (строка из цифр).

    Returns:
        Маска карты в формате "XXXX XX** **** XXXX".

    Examples:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    # Оставляем только цифры на случай, если номер передан с пробелами
    digits = "".join(ch for ch in card_number if ch.isdigit())

    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта.

    Отображает только последние 4 цифры, перед ними — две звёздочки.

    Args:
        account_number: Номер счёта (строка из цифр).

    Returns:
        Маска счёта в формате "**XXXX".

    Examples:
        >>> get_mask_account("73654108430135874305")
        '**4305'
    """
    digits = "".join(ch for ch in account_number if ch.isdigit())

    if len(digits) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")

    return f"**{digits[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
