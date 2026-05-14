"""
Модуль 2: Игровые персонажи.
Реализует систему классов персонажей с уникальными формулами характеристик.
"""

from module1_unit import Unit
from math import floor


class Character(Unit):
    """
    Класс игрока - персонаж, управляемый игроком.
    Поддерживает три архетипа: воин, маг, охотник.
    """
    
    ARCHETYPES = ('warrior', 'mage', 'hunter')
    
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class: str):
        """
        Создание персонажа с заданными характеристиками.
        
        Args:
            strength (int): Сила
            dexterity (int): Ловкость
            constitution (int): Телосложение
            wisdom (int): Мудрость
            intelligence (int): Интеллект
            charisma (int): Харизма
            character_class (str): Класс персонажа ('warrior', 'mage', 'hunter')
            
        Raises:
            ValueError: Если указан несуществующий класс
        """
        if character_class not in self.ARCHETYPES:
            raise ValueError(
                f"Недопустимый класс '{character_class}'. "
                f"Выберите один из: {', '.join(self.ARCHETYPES)}"
            )
        
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class
        
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.attack_power = self.calculate_damage()
        self.defense_rating = self.calculate_defense()
        
        self.max_mana = self.calculate_max_mana()
        self.mana_pool = self.max_mana

    def calculate_max_health(self) -> int:
        """
        Расчёт максимального здоровья (единая формула для всех классов).
        Формула: телосложение * 10 + сила // 2
        """
        health = self.constitution * 10 + self.strength // 2
        return floor(health)

    def calculate_damage(self) -> int:
        """
        Расчёт урона в зависимости от класса персонажа.
        """
        class_formulas = {
            'warrior': lambda: floor(self.strength * 2.2) + self.constitution // 3,
            'mage': lambda: floor(self.intelligence * 2.5) + self.wisdom // 2,
            'hunter': lambda: floor(self.dexterity * 1.9) + self.strength // 3
        }
        
        return class_formulas[self.character_class]()

    def calculate_defense(self) -> int:
        """
        Расчёт защиты в зависимости от класса персонажа.
        """
        class_formulas = {
            'warrior': lambda: floor(self.constitution * 1.8) + self.strength // 4,
            'mage': lambda: floor(self.wisdom * 1.3) + self.intelligence // 6,
            'hunter': lambda: floor(self.dexterity * 1.6) + self.constitution // 5
        }
        
        return class_formulas[self.character_class]()

    def calculate_max_mana(self) -> int:
        """
        Расчёт максимального запаса маны в зависимости от класса.
        """
        class_mana_formulas = {
            'warrior': lambda: self.intelligence + self.strength // 2,
            'mage': lambda: self.intelligence * 3 + self.wisdom,
            'hunter': lambda: floor(self.dexterity * 1.5) + self.wisdom // 2
        }
        
        return class_mana_formulas[self.character_class]()
    
    def get_class_name_russian(self) -> str:
        """Возвращает название класса на русском языке."""
        names = {
            'warrior': 'Воин',
            'mage': 'Маг',
            'hunter': 'Охотник'
        }
        return names.get(self.character_class, 'Неизвестный')
    
    def get_stats_summary(self) -> dict:
        """
        Возвращает сводку характеристик персонажа.
        
        Returns:
            dict: Словарь с основными параметрами
        """
        return {
            'class': self.get_class_name_russian(),
            'health': f"{self.current_health}/{self.max_health}",
            'mana': f"{self.mana_pool}/{self.max_mana}",
            'damage': self.attack_power,
            'defense': self.defense_rating
        }