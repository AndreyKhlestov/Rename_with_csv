import os
import re

from config import BASE_PATH, BASE_EXCLUDE_REGEX, BASE_INCLUDE_REGEX, logger
from objects import File
from work_with_csv import read_csv_file


def search_files(directory: str = BASE_PATH,
                 include_regex: str = BASE_INCLUDE_REGEX,
                 exclude_regex: str = BASE_EXCLUDE_REGEX
                 ) -> list:
    """Поиск файлов в указанной директории при помощи регулярных выражений"""
    compiled_include_regex = re.compile(include_regex)
    compiled_exclude_regex = re.compile(exclude_regex)
    result = list()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if compiled_include_regex.search(file) and not compiled_exclude_regex.search(file):
                result.append(File(root, file))
    return result


def rename_file(old_name: str, new_name: str, directory: str = BASE_PATH):
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    logger.info(f"Переименовал файл {old_name} в {new_name} в директории {directory}")


def main():
    logger.info("Запуск программы")

    # путь к файлу CSV, который нужно прочитать
    name_csv_file = "eBay-OrdersReport-Jun-28-2023-01_39_23-0700-13106848719.csv"
    csv_file_path = os.path.join(BASE_PATH, name_csv_file)  # возможно нужно будет отдельно получать путь

    # получаем словарь из короткого и длинного номера заказа
    orders = read_csv_file(csv_file_path)

    # получаем список файлов, которые подходят по шаблону для переименования
    files = search_files()

    # вытаскиваем номера заказов и ищем их в названиях файлов из полученного списка
    for order in orders:
        # Регулярное выражение для поиска файлов соответствующих заказу
        pattern = fr".+_{order.sales_number}_.+.eps$"

        # получаем файлы, относящиеся к заказу
        order_files = [file for file in files if re.search(pattern, file.name)]

        if order_files:
            for file in order_files:
                # current_name_file = os.path.join(file.directory, file.name)
                new_name = file.name.replace(f"_{order.sales_number}_", f"_{order.sales_number}_{order.order_number}_")
                # new_name_file = os.path.join(file.directory, new_name)
                rename_file(old_name=file.name, new_name=new_name, directory=file.directory)

    logger.info("Программа завершила работу")


if __name__ == '__main__':
    main()

# rename_file(current_name_file, new_name_file)
#
# path = os.listdir(BASE_PATH)
# for i_path in path:
#     print(i_path)
#
# # Пример использования функции:
# a = search_files()
# for i in a:
#     print(i)

