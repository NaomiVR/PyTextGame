# items/_ItemBase.py
class ItemBase:
    def __init__(self, name, description, amount, price, weight, _type):
        self._name = name
        self._description = description
        self._amount = amount
        self._price = price
        self._weight = weight
        self._type = _type

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Amount can't be negative.")
        self._amount = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        self._price = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight can't be negative.")
        self._weight = value

    def __str__(self):
        return f"{self._name}: {self._description}"

    def __repr__(self):
        return f"Item({self._name}, {self._description})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name and self._description == other._description

    def __hash__(self):
        return hash((self._name, self._description))
