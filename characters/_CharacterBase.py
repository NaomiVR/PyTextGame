# characters/_CharacterBase.py
from _types import DamageTypes


class Character:
    def __init__(self, name, health, attack, defense, attack_type, defense_type):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attack_type = attack_type
        self.defense_type = defense_type

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health can't be negative.")
        self._health = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        if value < 0:
            raise ValueError("Attack can't be negative.")
        self._attack = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        if value < 0:
            raise ValueError("Defense can't be negative.")
        self._defense = value

    def __str__(self):
        return f"{self.name}: Health={self.health}, Attack={self.attack}, Defense={self.defense}"

    def __repr__(self):
        return f"Character({self.name}, {self.health}, {self.attack}, {self.defense})"

    def __eq__(self, other):
        if isinstance(other, Character):
            return (self.name == other.name and
                    self.health == other.health and
                    self.attack == other.attack and
                    self.defense == other.defense)

    def __hash__(self):
        return hash((self.name, self.health, self.attack, self.defense))

    def take_damage(self, damage, other):
        match other.attack_type:
            case DamageTypes.PHYSICAL:
                if self.defense_type == DamageTypes.PHYSICAL:
                    self.health -= damage - self.defense
                else:
                    self.health -= damage
            case DamageTypes.MAGICAL:
                if self.defense_type == DamageTypes.MAGICAL:
                    self.health -= damage - self.defense
                else:
                    self.health -= damage
            case _:
                self.health -= damage
