# items/consumables/Consumables.py
from ._ConsumableBase import ConsumableBase
from ...custom_types import ItemTypes, ConsumableTypes


class HealthPotion(ConsumableBase):
    def __init__(self, amount):
        super().__init__("health potion", "Restores 50 Health Points", 1, 5.0,
                         0.1, ItemTypes.CONSUMABLE, ConsumableTypes.RESTORE)
