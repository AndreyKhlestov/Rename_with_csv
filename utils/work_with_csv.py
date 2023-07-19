import csv
import re

from config import logger
from objects import Order


def check_row_csv(row: list, index: int) -> bool:
    """Проверка корректности значений строки, полученной из csv файла"""
    # если строка пустая (находится перед последними двумя строками)
    if len(row[0]) == 0 and len(row[1]) == 0:
        return False

    # пропускаем последние две строки
    if row[0] == "Seller ID : denmary-print" or row[1] == "record(s) downloaded":
        return False

    correct_row = True
    # проверка sales_number
    if not row[0].isdigit() or len(row[0]) != 6:
        logger.warning(f"В {index} строке значение 'sales number' (1 столбец) "
                       f"должно состоять только из 6 цифр (без пробелов)")
        correct_row = False

    # проверка order number
    if not re.match(r"\d{2}-\d{5}-\d{5}", row[1]):
        logger.warning(f"В {index} строке значение 'Order number' (2 столбец) "
                       f"должно быть аналогично следующей записи: '09-10222-23678'")
        correct_row = False

    return correct_row


def read_csv_file(file_path: str) -> list:
    with open(file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        orders = list()

        # читаем построчно csv файл
        for index, row in enumerate(reader):
            # пропуск первых строк с заголовком и пустыми разделительными строками
            if index < 3:
                continue
            # проверка данных
            if not check_row_csv(row, index):
                continue

            new_order = Order(sales_number=row[0], order_number=row[1])
            if new_order not in orders:
                orders.append(new_order)

        # проверка наличия полученных данных о заказах
        if len(orders) == 0:
            logger.__error("Не получены данные о заказах из файла. Проверьте csv файл.")
            raise ValueError("Нет данных о заказах")

        return orders
