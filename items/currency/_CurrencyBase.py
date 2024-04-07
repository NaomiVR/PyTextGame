# items/currency/_CurrencyBase.py
from items import _ItemBase


class CurrencyBase(ItemBase):
    def __init__(self, name, description, amount, price, weight, _type):
        super().__init__(name, description, amount, price, weight, _type)
