# custom_types/ItemTypes.py
from enum import Enum


class ItemTypes(Enum):
    CURRENCY = 'Currency'
    WEAPON = 'Weapon'
    CONSUMABLE = 'Consumable'
    MISC = 'Miscellaneous'
    DUMMY = 'Placeholder'
