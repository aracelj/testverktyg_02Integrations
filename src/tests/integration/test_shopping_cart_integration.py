import pytest
from shoppingcart.shopping_cart import ShoppingCart
from shoppingcart.inventory import Inventory, OutOfStockError


def test_add_inventory_integration():
    cart = ShoppingCart()

    # Add a new item
    cart.add_inventory_item("banana", 2)
    assert cart.inventory["banana"] == 2

    # Add more of the same item
    cart.add_inventory_item("banana", 3)
    assert cart.inventory["banana"] == 5

    # Add another item
    cart.add_inventory_item("apple", 4)
    assert cart.inventory["apple"] == 4


"""  def test_cannot_add_item_not_in_stock():
    inventory = Inventory()
    cart = ShoppingCart(inventory)

    try:
        cart.add_inventory_item("grapes", 1)
        assert False, "Expected OutOfStockError"
    except OutOfStockError:
        assert True  """

def test_cannot_add_item_not_in_stock():
    inventory = Inventory()   # must be empty
    cart = ShoppingCart(inventory)

    assert inventory.is_in_stock("grapes", 1) is False  # debug check

    with pytest.raises(OutOfStockError):
        cart.add_inventory_item("grapes", 1)


