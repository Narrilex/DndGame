"""
Персонаж описывается:
- Имя
- Игровой/Непись
- Мировоззрение
- Уровень
- Количество опыта
- Профиенси бонус
- Характеристики (сила, ловкость, телосложение, интеллект, мудрость, харизма)
- Спасброски
- Пассивные характеристики
- Классовые фичи
- Расовые фичи
- Бекграундовые фичи
- Ресурсы (текущий АС, здоровье, скорость, хитдайсы)
- Инвентарь

"""

"""
0-базис: есть персонаж, у него есть шесть характеристик и базовые ресурсы (максимальное здоровье, броня, профиенси бонус и опыт)
"""

# Блок сборной сущности (токен, персонаж, монстр, непись)

class Token:
    def __init__(self):
        self.resources = Resources(10, 10, 0, 0)
        self.abilities = Abilities(10, 10, 10, 10, 10, 10)
    

class Character(Token):
    def __init__(self, Resources, Abilities):
        self.resources = Resources
        self.abilities = Abilities

# Блок характеристик

class Abilities:
    def __init__(self, value_strength, value_dexterity, value_constitution, value_intelligence, value_wisdom, value_charisma):
        self.strength = Ability("Strength", value_strength)
        self.dexterity = Ability("Dexterity", value_dexterity)
        self.constitution = Ability("Constitution", value_constitution)
        self.intelligence = Ability("Intelligence", value_intelligence)
        self.wisdom = Ability("Wisdom", value_wisdom)
        self.charisma = Ability("Charisma", value_charisma)

class Ability:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.modifier = (value-10)//2

# Блок ресурсов

class Resources:
    def __init__(self, max_HP, AC, PB, XP):
        self.max_HP = Resource("max_HP", max_HP) 
        self.AC = Resource("AC", AC)
        self.PB = Resource("PB", PB)
        self.XP = Resource("XP", XP)

class Resource:
    def __init__(self, name, value):
        self.name = name
        self.value = value


Jhon = Character(Resources(20, 15, 2, 0), Abilities(15, 14, 13, 12, 10, 8))
print("Jhon's hp are " + str(Jhon.resources.max_HP.value))
print("Jhon's Strength value is " + str(Jhon.abilities.strength.value))
print("Jhon's Strength modifier is " + str(Jhon.abilities.strength.modifier))

SomeToken = Token()
print("SomeToken's hp are " + str(SomeToken.resources.max_HP.value))
print("SomeToken's Strength value is " + str(SomeToken.abilities.strength.value))
print("SomeToken's Strength modifier is " + str(SomeToken.abilities.strength.modifier))