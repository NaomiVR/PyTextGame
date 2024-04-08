# items/currency/_CurrencyBase.pyi
from ..ItemBase import ItemBase
from ...custom_types import CurrencyTypes


class CurrencyBase(ItemBase):
    def __init__(self, name: str, description: str, amount: int,
                 price: float, weight: float, _type: CurrencyTypes) -> None: ...
