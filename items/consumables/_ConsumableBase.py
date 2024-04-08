# items/_ConsumableBase.py
from ..ItemBase import ItemBase


class ConsumableBase(ItemBase):
    def __init__(self, name, description, amount, price, weight, item_type, _type):
        super().__init__(name, description, amount, price, weight, item_type, _type)

    def use(self):
        if self._amount > 0:
            self._amount -= 1
        else:
            raise ValueError("No more items left to consume.")
