# items/weapons/Weapons.py
from ._WeaponBase import WeaponBase
from ...custom_types import ItemTypes, DamageTypes


class Excalibur(WeaponBase):
    def __init__(self):
        super().__init__("Excalibur", "The legendary sword of King Arthur.", 1, 50.5,
                         5.5, 50, ItemTypes.WEAPON, DamageTypes.PHYSICAL)


class Mjolnir(WeaponBase):
    def __init__(self):
        super().__init__("Mjolnir", "The mighty hammer of Thor.", 1, 60.5,
                         6.0, 60, ItemTypes.WEAPON, DamageTypes.MAGICAL)


class Gungnir(WeaponBase):
    def __init__(self):
        super().__init__("Gungnir", "The spear of Odin.", 1, 55.5,
                         5.5, 55, ItemTypes.WEAPON, DamageTypes.PHYSICAL)


class Trident(WeaponBase):
    def __init__(self):
        super().__init__("Trident", "The three-pronged spear of Poseidon.", 1, 58.5,
                         5.8, 58, ItemTypes.WEAPON, DamageTypes.PHYSICAL)


class BowOfArtemis(WeaponBase):
    def __init__(self):
        super().__init__("BowOfArtemis", "The bow of the goddess Artemis.", 1, 52.5,
                         5.2, 52, ItemTypes.WEAPON, DamageTypes.MAGICAL)
