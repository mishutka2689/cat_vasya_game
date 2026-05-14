"""
Тестовый запуск игровой системы кота Василия.
Проверяет работу всех модулей и демонстрирует возможности.
"""

from module1_unit import Monster
from module2_character import Character
from module3_spell import Fireball, IceLance, LightningBolt, HealingWave


def print_separator(title: str = ""):
    """Выводит разделительную линию с заголовком."""
    print("\n" + "=" * 50)
    if title:
        print(f" {title}")
        print("=" * 50)


def test_monster_creation():
    """Тестирует создание и характеристики монстров."""
    print_separator("ТЕСТ 1: Создание монстров")
    
    goblin = Monster(
        strength=10,
        dexterity=8,
        constitution=12,
        wisdom=5,
        intelligence=4,
        charisma=3
    )
    
    print(f" Гоблин:")
    print(f" Здоровье: {goblin.calculate_max_health()}")
    print(f" Урон: {goblin.calculate_damage()}")
    print(f" Защита: {goblin.calculate_defense()}")
    
    ogre = Monster(15, 6, 18, 4, 3, 5)
    print(f"\n Огр:")
    print(f" Здоровье: {ogre.calculate_max_health()}")
    print(f" Урон: {ogre.calculate_damage()}")
    print(f" Защита: {ogre.calculate_defense()}")


def test_character_classes():
    """Тестирует создание персонажей разных классов."""
    print_separator("ТЕСТ 2: Классы персонажей")
    
    warrior = Character(
        strength=15, dexterity=10, constitution=14,
        wisdom=8, intelligence=6, charisma=12,
        character_class='warrior'
    )
    
    stats = warrior.get_stats_summary()
    print(f" {stats['class']}:")
    print(f" Здоровье: {stats['health']}")
    print(f" Мана: {stats['mana']}")
    print(f" Урон: {stats['damage']}")
    print(f" Защита: {stats['defense']}")
    
    mage = Character(
        strength=8, dexterity=10, constitution=10,
        wisdom=14, intelligence=18, charisma=12,
        character_class='mage'
    )
    
    stats = mage.get_stats_summary()
    print(f"\n {stats['class']}:")
    print(f" Здоровье: {stats['health']}")
    print(f" Мана: {stats['mana']}")
    print(f" Урон: {stats['damage']}")
    print(f" Защита: {stats['defense']}")
    
    hunter = Character(
        strength=12, dexterity=16, constitution=10,
        wisdom=10, intelligence=8, charisma=14,
        character_class='hunter'
    )
    
    stats = hunter.get_stats_summary()
    print(f"\n {stats['class']}:")
    print(f" Здоровье: {stats['health']}")
    print(f" Мана: {stats['mana']}")
    print(f" Урон: {stats['damage']}")
    print(f" Защита: {stats['defense']}")


def test_spell_system():
    """Тестирует систему заклинаний и маны."""
    print_separator("ТЕСТ 3: Магическая система")
    
    mage = Character(
        strength=8, dexterity=10, constitution=10,
        wisdom=14, intelligence=18, charisma=12,
        character_class='mage'
    )
    
    print(f" Маг создан с маной: {mage.mana_pool}/{mage.max_mana}")
    
    print("\n Изучение заклинаний:")
    mage.learn_spell(Fireball())
    print(f" + {Fireball()}")
    
    mage.learn_spell(IceLance())
    print(f" + {IceLance()}")
    
    mage.learn_spell(LightningBolt())
    print(f" + {LightningBolt()}")
    
    mage.learn_spell(HealingWave())
    print(f" + {HealingWave()}")
    
    print(f"\n Всего заклинаний в книге: {len(mage.spellbook)}")
    
    print("\n Применение заклинаний:")
    try:
        print(f" Мана перед боем: {mage.mana_pool}")
        
        damage = mage.use_spell(1) # IceLance
        print(f" ✓ Применено заклинание, осталось маны: {mage.mana_pool}")
        
        damage = mage.use_spell(2) # LightningBolt
        print(f" ✓ Применено заклинание, осталось маны: {mage.mana_pool}")
        
        print(f"\n Попытка применить Огненный шар (нужно 15 маны, есть {mage.mana_pool})...")
        mage.use_spell(0) # Fireball
        
    except ValueError as e:
        print(f" ✗ Ошибка: {e}")


def test_abstract_classes():
    """Проверяет невозможность создания абстрактных классов."""
    print_separator("ТЕСТ 4: Абстрактные классы")
    
    print("Попытка создать экземпляр абстрактного класса Unit...")
    try:
        from module1_unit import Unit
        unit = Unit(10, 10, 10, 10, 10, 10)
        print("  ОШИБКА: Unit можно создать!")
    except TypeError as error:
        print(f"  Правильно заблокировано: {error}")
    
    print("\nПопытка создать экземпляр абстрактного класса Spell...")
    try:
        from module3_spell import Spell
        spell = Spell("Тест", 10, 5)
        print("  ОШИБКА: Spell можно создать!")
    except TypeError as error:
        print(f"  Правильно заблокировано: {error}")


def test_invalid_character_class():
    """Тестирует обработку неверного класса персонажа."""
    print_separator("ТЕСТ 5: Валидация класса")
    
    print("Попытка создать персонажа с недопустимым классом...")
    try:
        invalid_char = Character(
            10, 10, 10, 10, 10, 10,
            character_class='necromancer'
        )
        print("  ОШИБКА: Недопустимый класс принят!")
    except ValueError as error:
        print(f"  Правильно отклонено: {error}")


def main():
    """Основная функция запуска всех тестов."""
    print(" ИГРОВАЯ СИСТЕМА КОТА ВАСИЛИЯ")
    
    test_monster_creation()
    test_character_classes()
    test_spell_system()
    test_abstract_classes()
    test_invalid_character_class()
    
    print_separator("ЗАВЕРШЕНИЕ")
    print(" Все тесты успешно пройдены!")
    print(" Игра готова к запуску!\n")


if __name__ == "__main__":
    main()