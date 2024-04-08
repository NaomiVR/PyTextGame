# items/currency/_CurrencyBase.py
from ..ItemBase import ItemBase


class CurrencyBase(ItemBase):
    def __init__(self, name, description, amount, price, weight, item_type, _type):
        super().__init__(name, description, amount, price, weight, item_type, _type)
