# items/_ConsumableBase.pyi
from ..ItemBase import ItemBase
from ...custom_types import ItemTypes, ConsumableTypes

class ConsumableBase(ItemBase):
    def __init__(self, name: str, description: str, amount: int, price: float,
                 weight: float, item_type: ItemTypes, _type: ConsumableTypes) -> None: ...
    def use(self) -> None: ...
