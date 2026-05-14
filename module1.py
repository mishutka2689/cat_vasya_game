"""
Module 1: Abstract Unit class and Monster implementation.
Defines base stats and abstract methods for game entities.
"""

from abc import ABC, abstractmethod
import math


class Unit(ABC):
    """Abstract base class for all game units."""
    
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        # Для системы заклинаний (модуль 3)
        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Calculate maximum health points."""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Calculate base damage output."""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Calculate defense rating."""
        pass

    def add_spell(self, spell) -> None:
        """Add a spell to unit's spellbook."""
        self.spells.append(spell)

    def cast_spell(self, index: int):
        """Cast a spell by index if enough mana."""
        if index < 0 or index >= len(self.spells):
            raise IndexError("Spell index out of range")
        
        spell = self.spells[index]
        if self.mana < spell.mana_cost:
            raise ValueError(f"Not enough mana! Need {spell.mana_cost}, have {self.mana}")
        
        self.mana -= spell.mana_cost
        return spell.cast()


class Monster(Unit):
    """Monster class implementing Unit abstract methods."""
    
    def calculate_max_health(self) -> int:
        # constitution * 8 + strength // 3
        return self.constitution * 8 + self.strength // 3

    def calculate_damage(self) -> int:
        # strength * 2 + constitution // 5
        return self.strength * 2 + self.constitution // 5

    def calculate_defense(self) -> int:
        # constitution * 1.2 + strength // 5
        return int(self.constitution * 1.2) + self.strength // 5