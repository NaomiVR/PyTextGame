# characters/_CharacterBase.pyi
from typing import Any
from ..custom_types import DamageTypes


class CharacterBase:
    name: str
    _health: int
    _attack: int
    _defense: int

    def __init__(self, name: str, health: int, attack: int, defense: int,
                 attack_type: DamageTypes, defense_type: DamageTypes) -> None: ...

    @property
    def health(self) -> int: ...
    @health.setter
    def health(self, value: int) -> None: ...
    @property
    def attack(self) -> int: ...
    @attack.setter
    def attack(self, value: int) -> None: ...
    @property
    def defense(self) -> int: ...
    @defense.setter
    def defense(self, value: int) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def TakeDamage(self, damage: int, other: Any) -> None: ...
    def is_alive(self) -> bool: ...
