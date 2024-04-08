# items/weapons/_WeaponBase.pyi
from ..ItemBase import ItemBase
from ...custom_types import DamageTypes


class WeaponBase(ItemBase):
    _damage: int

    def __init__(self, damage: int, name: str, description: str, amount: int,
                 price: float, weight: float, _type: DamageTypes) -> None: ...
    @property
    def damage(self) -> int: ...
    @damage.setter
    def damage(self, value: int) -> None: ...
