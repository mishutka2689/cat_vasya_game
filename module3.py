"""
Модуль 3: Магическая система.
Определяет абстрактные и конкретные заклинания для использования в бою.
"""

from abc import ABC, abstractmethod


class Spell(ABC):
    """
    Абстрактный базовый класс для всех магических заклинаний.
    Определяет интерфейс применения магии.
    """
    
    def __init__(self, name: str, damage: int, mana_cost: int):
        """
        Инициализация заклинания.
        
        Args:
            name (str): Название заклинания
            damage (int): Базовый урон
            mana_cost (int): Стоимость применения в манах
        """
        self.spell_name = name
        self.base_damage = damage
        self.required_mana = mana_cost

    @abstractmethod
    def activate(self) -> int:
        """
        Активирует заклинание.
        
        Returns:
            int: Нанесённый урон
        """
        pass
    
    def __str__(self) -> str:
        """Строковое представление заклинания."""
        return f"{self.spell_name} (Урон: {self.base_damage}, Мана: {self.required_mana})"


class Fireball(Spell):
    """
    Огненный шар - классическое атакующее заклинание.
    Наносит высокий урон за среднюю стоимость маны.
    """
    
    def __init__(self):
        super().__init__(
            name="Огненный шар",
            damage=35,
            mana_cost=15
        )
    
    def activate(self) -> int:
        """Применяет огненный шар и возвращает урон."""
        print(f" {self.spell_name} наносит {self.base_damage} урона!")
        return self.base_damage


class IceLance(Spell):
    """
    Ледяное копьё - быстрое заклинание с низким расходом маны.
    Идеально для частого использования.
    """
    
    def __init__(self):
        super().__init__(
            name="Ледяное копьё",
            damage=25,
            mana_cost=10
        )
    
    def activate(self) -> int:
        """Применяет ледяное копьё и возвращает урон."""
        print(f" {self.spell_name} наносит {self.base_damage} урона!")
        return self.base_damage


class LightningBolt(Spell):
    """
    Удар молнии - мощнейшее заклинание с высоким расходом маны.
    Способно изменить ход боя.
    """
    
    def __init__(self):
        super().__init__(
            name="Удар молнии",
            damage=40,
            mana_cost=20
        )
    
    def activate(self) -> int:
        """Применяет удар молнии и возвращает урон."""
        print(f" {self.spell_name} наносит {self.base_damage} урона!")
        return self.base_damage


class HealingWave(Spell):
    """
    Целебная волна - заклинание восстановления (бонусное).
    """
    
    def __init__(self):
        super().__init__(
            name="Целебная волна",
            damage=0,
            mana_cost=12
        )
    
    def activate(self) -> int:
        """Применяет лечение."""
        print(f" {self.spell_name} восстанавливает здоровье!")
        return self.base_damage