# characters/player/_PlayerBase.py
from ._Inventory import Inventory
from .._CharacterBase import CharacterBase


class PlayerBase(CharacterBase):
    def __init__(self, name, health, attack, defense, attack_type, defense_type, weight_limit):
        super().__init__(name, health, attack, defense, attack_type, defense_type)
        self.inventory = Inventory()
        self.weight = weight_limit
