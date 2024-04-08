# items/weapons/_WeaponBase.py
from ..ItemBase import ItemBase


class WeaponBase(ItemBase):
    def __init__(self, name, description, amount, price, weight, damage, item_type, _type):
        super().__init__(name, description, amount, price, weight, item_type, _type)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if value < 0:
            raise ValueError("Damage can't be negative.")
        self._damage = value
