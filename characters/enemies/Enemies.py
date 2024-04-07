# characters/enemies/Enemies.py
from . import _EnemyBase
from _types import DamageTypes


class Dragon(_EnemyBase):
    def __init__(self):
        super().__init__("Dragon", 100, 20, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Griffin(_EnemyBase):
    def __init__(self):
        super().__init__("Griffin", 80, 15, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Phoenix(_EnemyBase):
    def __init__(self):
        super().__init__("Phoenix", 70, 18, 8, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Unicorn(_EnemyBase):
    def __init__(self):
        super().__init__("Unicorn", 60, 12, 10, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Minotaur(_EnemyBase):
    def __init__(self):
        super().__init__("Minotaur", 90, 22, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Centaur(_EnemyBase):
    def __init__(self):
        super().__init__("Centaur", 85, 18, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Hydra(_EnemyBase):
    def __init__(self):
        super().__init__("Hydra", 110, 25, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Cyclops(_EnemyBase):
    def __init__(self):
        super().__init__("Cyclops", 95, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Siren(_EnemyBase):
    def __init__(self):
        super().__init__("Siren", 70, 15, 10, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Medusa(_EnemyBase):
    def __init__(self):
        super().__init__("Medusa", 80, 18, 12, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Sphinx(_EnemyBase):
    def __init__(self):
        super().__init__("Sphinx", 85, 20, 15, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Chimera(_EnemyBase):
    def __init__(self):
        super().__init__("Chimera", 90, 22, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Harpy(_EnemyBase):
    def __init__(self):
        super().__init__("Harpy", 75, 15, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Basilisk(_EnemyBase):
    def __init__(self):
        super().__init__("Basilisk", 80, 18, 8, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Kraken(EnemyBase):
    def __init__(self):
        super().__init__("Kraken", 100, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Gorgon(_EnemyBase):
    def __init__(self):
        super().__init__("Gorgon", 85, 18, 10, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Nymph(_EnemyBase):
    def __init__(self):
        super().__init__("Nymph", 70, 15, 12, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Satyr(_EnemyBase):
    def __init__(self):
        super().__init__("Satyr", 75, 15, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Pegasus(_EnemyBase):
    def __init__(self):
        super().__init__("Pegasus", 80, 18, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Cerberus(_EnemyBase):
    def __init__(self):
        super().__init__("Cerberus", 90, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)
