# items/currency/_CurrencyBase.pyi
from ..ItemBase import ItemBase
from ...custom_types import ItemTypes, CurrencyTypes


class CurrencyBase(ItemBase):
    def __init__(self, name: str, description: str, amount: int, price: float,
                 weight: float, item_type: ItemTypes, _type: CurrencyTypes) -> None: ...
