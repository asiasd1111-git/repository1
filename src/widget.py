"""Модуль для работы с виджетом банковских операций."""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счёта в строке с типом.

    Принимает строку вида "Visa Platinum 7000792289606361" или
    "Счет 73654108430135874305" и возвращает строку с замаскированным
    номером, сохраняя тип и название.

    Args:
        account_info: Строка с типом и номером карты/счёта.

    Returns:
        Строка с замаскированным номером.

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    # Разделяем строку на части по пробелам
    parts = account_info.split()

    # Последняя часть — номер, всё остальное — тип/название
    number = parts[-1]
    name = " ".join(parts[:-1])

    # Определяем тип: счёт или карта
    if "счет" in name.lower() or "account" in name.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формат "ДД.ММ.ГГГГ".

    Args:
        date_string: Дата в ISO-формате, например
            "2024-03-11T02:26:18.671407".

    Returns:
        Дата в формате "ДД.ММ.ГГГГ".

    Examples:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    parsed = datetime.fromisoformat(date_string)
    return parsed.strftime("%d.%m.%Y")
