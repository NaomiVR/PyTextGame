# items/weapons/_WeaponBase.py
from items import _ItemBase


class WeaponBase(_ItemBase):
    def __init__(self, damage, name, description, amount, price, weight, _type):
        super().__init__(name, description, amount, price, weight, _type)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if value < 0:
            raise ValueError("Damage can't be negative.")
        self._damage = value
