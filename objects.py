class File:
    """Класс для хранения информации о файле"""
    def __init__(self, directory: str, name: str):
        self.directory = directory
        self.name = name

    def __str__(self):
        return self.name


class Order:
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
