# items/currency/Currencies.py
from ._CurrencyBase import CurrencyBase
from ...custom_types import ItemTypes, CurrencyTypes


class Platinum(CurrencyBase):
    def __init__(self, amount):
        super().__init__("Platinum", "A coin made out of a rare material with a large value", amount,
                         0, 0, ItemTypes.CURRENCY, CurrencyTypes.PLATINUM)

    def to_gold(self):
        return self.amount * 10

    def to_silver(self):
        return self.to_gold() * 10

    def to_bronze(self):
        return self.to_silver() * 10


class Gold(CurrencyBase):
    def __init__(self, amount):
        super().__init__("Gold", "A coin made out of a rare material with a decent value", amount,
                         0, 0, ItemTypes.CURRENCY, CurrencyTypes.GOLD)

    def to_platinum(self):
        return self.amount / 10

    def to_silver(self):
        return self.amount * 10

    def to_bronze(self):
        return self.to_silver() * 10


class Silver(CurrencyBase):
    def __init__(self, amount):
        super().__init__("Silver", "A coin made out of a rare material with an average value", amount,
                         0, 0, ItemTypes.CURRENCY, CurrencyTypes.SILVER)

    def to_platinum(self):
        return self.to_gold() / 10

    def to_gold(self):
        return self.amount / 10

    def to_bronze(self):
        return self.amount * 10


class Bronze(CurrencyBase):
    def __init__(self, amount):
        super().__init__("Bronze", "A coin made out of a rare material with a weak value", amount,
                         0, 0, ItemTypes.CURRENCY, CurrencyTypes.BRONZE)

    def to_platinum(self):
        return self.to_gold() / 10

    def to_gold(self):
        return self.to_silver() / 10

    def to_silver(self):
        return self.amount / 10
