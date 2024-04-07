# items/currency/_CurrencyBase.pyi
from items import _ItemBase
from _types import CurrencyTypes


class CurrencyBase(_ItemBase):
    def __init__(self, name: str, description: str, amount: int,
                 price: float, weight: float, _type: CurrencyTypes) -> None: ...
