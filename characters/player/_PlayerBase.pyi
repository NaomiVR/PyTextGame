# characters/player/_PlayerBase.pyi
from characters import _CharacterBase
from . import _Inventory
from _types import DamageTypes


class PlayerBase(CharacterBase):
    _invetory: _Inventory
    _weight_limit: float

    def __init__(self, name: str, health: int, attack: int, defense: int,
                 attack_type: DamageTypes, defense_type: DamageTypes, weight_limit: float) -> None: ...
