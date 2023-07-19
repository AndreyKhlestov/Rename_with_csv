import re

from config import CSV_FILE_PATH, logger, INFO, BASE_INCLUDE_REGEX
from utils.work_with_csv import read_csv_file
from utils.work_with_file import search_files, rename_file


def main():
    # получаем список заказов из файла
    orders = read_csv_file(CSV_FILE_PATH)
    # получаем список файлов, которые подходят по шаблону для переименования
    files = search_files()

    # вытаскиваем номера заказов и ищем их в названиях файлов из полученного списка
    for order in orders:
        # Регулярное выражение для поиска файлов соответствующих заказу (заменяем часть шаблона на реальный номер)
        pattern = BASE_INCLUDE_REGEX.pattern.replace(r"\d{6}", order.sales_number)

        # получаем файлы, относящиеся к заказу
        order_files = [file for file in files if re.search(pattern, file.name)]

        if order_files:
            for file in order_files:
                new_name = file.name.replace(f"_{order.sales_number}_", f"_{order.sales_number}_{order.order_number}_")
                rename_file(old_name=file.name, new_name=new_name, directory=file.directory)

                # удаляем данные файла, чтобы повторно его не использовать при поиске и
                # чтобы далее не засчитывать его как не переименованный файл
                files.remove(file)

    if len(files) > 0:
        for file in files:
            INFO.add_unknown_file(file.name)

    print(INFO)  # Вывод информации о работе программы
    logger.debug("Программа завершила работу")
    # input("Нажмите любую клавишу для закрытия программы")


if __name__ == '__main__':
    main()
