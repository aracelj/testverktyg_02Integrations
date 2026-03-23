class OutOfStockError(Exception):
    pass

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, item, amount):
        self.stock[item] = amount

    def is_in_stock(self, item, amount):
        return self.stock.get(item, 0) >= amount

    def reduce_stock(self, item, amount):
        if not self.is_in_stock(item, amount):
            raise OutOfStockError(f"{item} is not in stock")
        self.stock[item] -= amount