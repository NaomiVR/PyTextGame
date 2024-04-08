# custom_types/ConsumableTypes.py
from enum import Enum


class ConsumableType(Enum):
    RESTORE = 'Restoration Potions'
    BUFF = 'Buff Potions'
    DEBUFF = 'Debuff Potions'
