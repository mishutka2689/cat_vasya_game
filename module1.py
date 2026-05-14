"""
Модуль 1: Базовые игровые сущности.
Содержит абстрактный класс для всех юнитов и реализацию монстров.
"""

from abc import ABC, abstractmethod
from math import floor


class Unit(ABC):
    """
    Абстрактный базовый класс для всех существ в игре.
    Определяет основные характеристики и интерфейс для расчёта боевых параметров.
    """
    
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        """
        Инициализация характеристик юнита.
        
        Args:
            strength (int): Сила
            dexterity (int): Ловкость
            constitution (int): Телосложение
            wisdom (int): Мудрость
            intelligence (int): Интеллект
            charisma (int): Харизма
        """
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        
        self.spellbook = []
        self.mana_pool = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        """Вычисляет максимальное количество здоровья."""
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        """Вычисляет базовый урон юнита."""
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        """Вычисляет показатель защиты."""
        pass

    def learn_spell(self, spell) -> None:
        """
        Добавляет заклинание в книгу заклинаний юнита.
        
        Args:
            spell: Объект заклинания класса Spell
        """
        self.spellbook.append(spell)

    def use_spell(self, spell_index: int):
        """
        Применяет заклинание по индексу при достаточном количестве маны.
        
        Args:
            spell_index (int): Индекс заклинания в книге
            
        Returns:
            int: Урон от заклинания
            
        Raises:
            IndexError: Если индекс выходит за границы
            ValueError: Если недостаточно маны
        """
        if not (0 <= spell_index < len(self.spellbook)):
            raise IndexError(f"Заклинание под индексом {spell_index} не найдено")
        
        selected_spell = self.spellbook[spell_index]
        
        if self.mana_pool < selected_spell.mana_cost:
            raise ValueError(
                f"Недостаточно маны! Требуется: {selected_spell.mana_cost}, "
                f"доступно: {self.mana_pool}"
            )
        
        self.mana_pool -= selected_spell.mana_cost
        return selected_spell.activate()


class Monster(Unit):
    """
    Класс монстра - враждебной игровой сущности.
    Реализует формулы расчёта характеристик для чудовищ.
    """
    
    def calculate_max_health(self) -> int:
        health = self.constitution * 8 + self.strength // 3
        return floor(health)

    def calculate_damage(self) -> int:
        damage = self.strength * 2 + self.constitution // 5
        return floor(damage)

    def calculate_defense(self) -> int:
        defense = self.constitution * 1.2 + self.strength // 5
        return floor(defense)