# items/currency/Currencies.py
from _types import CurrencyTypes
from . import _CurrencyBase


class Platinum(CurrencyBase):
    def __init__(self, name, description, amount):
        super().__init__(name, description, amount, 0, 0, CurrencyTypes.PLATINUM)
        self.name = "Platinum"
        self.description = "A coin made out of a rare material with a large value"

    def to_gold(self):
        return self.amount * 10

    def to_silver(self):
        return self.to_gold() * 10

    def to_bronze(self):
        return self.to_silver() * 10


class Gold(CurrencyBase):
    def __init__(self, name, description, amount):
        super().__init__(name, description, amount, 0, 0, CurrencyTypes.GOLD)
        self.name = "Gold"
        self.description = "A coin made out of a rare material with a decent value"

    def to_platinum(self):
        return self.amount / 10

    def to_silver(self):
        return self.amount * 10

    def to_bronze(self):
        return self.to_silver() * 10


class Silver(CurrencyBase):
    def __init__(self, name, description, amount):
        super().__init__(name, description, amount, 0, 0, CurrencyTypes.SILVER)
        self.name = "Silver"
        self.description = "A coin made out of a rare material with an average value"

    def to_platinum(self):
        return self.to_gold() / 10

    def to_gold(self):
        return self.amount / 10

    def to_bronze(self):
        return self.amount * 10


class Bronze(CurrencyBase):
    def __init__(self, name, description, amount):
        super().__init__(name, description, amount, 0, 0, CurrencyTypes.BRONZE)
        self.name = "Bronze"
        self.description = "A coin made out of a rare material with a weak value"

    def to_platinum(self):
        return self.to_gold() / 10

    def to_gold(self):
        return self.to_silver() / 10

    def to_silver(self):
        return self.amount / 10
