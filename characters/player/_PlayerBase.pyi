# characters/player/_PlayerBase.pyi
from ._Inventory import Inventory
from .._CharacterBase import CharacterBase
from ...custom_types import DamageTypes


class PlayerBase(CharacterBase):
    inventory: Inventory()
    _weight_limit: float

    def __init__(self, name: str, health: int, attack: int, defense: int,
                 attack_type: DamageTypes, defense_type: DamageTypes, weight_limit: float) -> None: ...
