# characters/enemies/Enemies.py
from ._EnemyBase import EnemyBase
from ...custom_types import DamageTypes


class Dragon(EnemyBase):
    def __init__(self):
        super().__init__("Dragon", 100, 20, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Griffin(EnemyBase):
    def __init__(self):
        super().__init__("Griffin", 80, 15, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Phoenix(EnemyBase):
    def __init__(self):
        super().__init__("Phoenix", 70, 18, 8, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Unicorn(EnemyBase):
    def __init__(self):
        super().__init__("Unicorn", 60, 12, 10, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Minotaur(EnemyBase):
    def __init__(self):
        super().__init__("Minotaur", 90, 22, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Centaur(EnemyBase):
    def __init__(self):
        super().__init__("Centaur", 85, 18, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Hydra(EnemyBase):
    def __init__(self):
        super().__init__("Hydra", 110, 25, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Cyclops(EnemyBase):
    def __init__(self):
        super().__init__("Cyclops", 95, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Siren(EnemyBase):
    def __init__(self):
        super().__init__("Siren", 70, 15, 10, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Medusa(EnemyBase):
    def __init__(self):
        super().__init__("Medusa", 80, 18, 12, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Sphinx(EnemyBase):
    def __init__(self):
        super().__init__("Sphinx", 85, 20, 15, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Chimera(EnemyBase):
    def __init__(self):
        super().__init__("Chimera", 90, 22, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Harpy(EnemyBase):
    def __init__(self):
        super().__init__("Harpy", 75, 15, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Basilisk(EnemyBase):
    def __init__(self):
        super().__init__("Basilisk", 80, 18, 8, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Kraken(EnemyBase):
    def __init__(self):
        super().__init__("Kraken", 100, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Gorgon(EnemyBase):
    def __init__(self):
        super().__init__("Gorgon", 85, 18, 10, DamageTypes.MAGICAL, DamageTypes.PHYSICAL)


class Nymph(EnemyBase):
    def __init__(self):
        super().__init__("Nymph", 70, 15, 12, DamageTypes.MAGICAL, DamageTypes.MAGICAL)


class Satyr(EnemyBase):
    def __init__(self):
        super().__init__("Satyr", 75, 15, 10, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Pegasus(EnemyBase):
    def __init__(self):
        super().__init__("Pegasus", 80, 18, 12, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)


class Cerberus(EnemyBase):
    def __init__(self):
        super().__init__("Cerberus", 90, 20, 15, DamageTypes.PHYSICAL, DamageTypes.PHYSICAL)
