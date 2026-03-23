from shoppingcart.inventory import OutOfStockError

""" class ShoppingCart:
    def __init__(self):
        self.inventory = {}

    def add_inventory_item(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount """

class InventoryItem:
    def __init__(self, id, name, price, amount_in_stock):
        pass

class CartItem:
    def __init__(self, id, name, price, amount_in_cart):
        pass


class ShoppingCart:
    def __init__(self, inventory= None):
        self.inventory = inventory
        self.items = {}

    def add_inventory_item(self, item, amount):
        #if not self.inventory.is_in_stock(item, amount):
        #    raise OutOfStockError(f"{item} is not in stock")
        if not self.inventory.is_in_stock(item, amount):
            return False  # instead of raising

        self.inventory.reduce_stock(item, amount)
        self.items[item] = self.items.get(item, 0) + amount
        return True