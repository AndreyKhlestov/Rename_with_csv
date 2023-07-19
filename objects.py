class File:
    """Класс для хранения информации о файле"""
    def __init__(self, directory: str, name: str):
        self.directory = directory
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, File):
            return self.directory == other.directory and self.name == other.name
        return False

    def __repr__(self):
        return f"File('{self.directory}', '{self.name}')"


class Order:
    """Класс для хранения и сравнивание информации о заказах"""
    def __init__(self, sales_number: str, order_number: str):
        self.sales_number = sales_number
        self.order_number = order_number

    def __eq__(self, other):
        if isinstance(other, Order):
            return (
                    self.sales_number == other.sales_number and
                    self.order_number == other.order_number
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Info:
    """Класс для хранения и вывода информации о результатах выполнения программы"""
    def __init__(self) -> None:
        self.__rename_files = list()
        self.__unknown_files = list()
        self.__error = list()

    def add_error(self, text_error: str) -> None:
        self.__error.append(text_error)

    def add_unknown_file(self, file_name: str) -> None:
        self.__unknown_files.append(file_name)

    def add_rename_file(self, file_name: str) -> None:
        self.__rename_files.append(file_name)

    def __str__(self) -> str:
        first_block = self.__info_block__("Успешно переименованных файлов", self.__rename_files)
        second_block = self.__info_block__("Не переименовано", self.__unknown_files)
        third_block = self.__info_block__("Ошибок", self.__error)
        return "\n".join([first_block, second_block, third_block, "Программа завершила работу"])

    @staticmethod
    def __info_block__(text: str, block: list) -> str:
        main_text = f"{text}: {len(block)}"
        detail = " " * 4 + ("\n" + " " * 4).join(block) + "\n" if len(block) > 0 else ""
        return "\n".join([main_text, detail])
