# characters/enemies/_EnemyBase.py
from .._CharacterBase import CharacterBase


class EnemyBase(CharacterBase):
    def __init__(self, name, health, attack, defense, attack_type, defense_type):
        super().__init__(name, health, attack, defense, attack_type, defense_type)
