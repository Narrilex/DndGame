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
1-базис: у персонажа есть раса, раса даёт бонус к характеристикам и имеет какие-то свои трейты
"""

# Блок сборной сущности (токен, персонаж, монстр, непись)

class Token:
    def __init__(self):
        self.resources = Resources(10, 10, 0, 0)
        self.abilities = Abilities(10, 10, 10, 10, 10, 10)
    

class Character(Token):
    def __init__(self, Resources, AbilityValues, RaceName):
        self.RaceName = RaceName
        self.RacialTraits = RacialTraits(RaceName)
        self.resources = Resources
        self.abilities = Abilities(AbilityValues, self.RacialTraits.AbilityScoreIncrease) 

# Блок характеристик

class Abilities:
    def __init__(self, AbilityValues  = [10, 10, 10, 10, 10, 10], ability_score_increases = [0, 0, 0, 0, 0, 0]):
        self.strength = Ability("Strength", AbilityValues[0]+ability_score_increases[0])
        self.dexterity = Ability("Dexterity", AbilityValues[1]+ability_score_increases[1])
        self.constitution = Ability("Constitution", AbilityValues[2]+ability_score_increases[2])
        self.intelligence = Ability("Intelligence", AbilityValues[3]+ability_score_increases[3])
        self.wisdom = Ability("Wisdom", AbilityValues[4]+ability_score_increases[4])
        self.charisma = Ability("Charisma", AbilityValues[5]+ability_score_increases[5])

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


# Блок расовые трейты

class RacialTraits:
    def __init__(self, RaceName) -> None:
        if RaceName == "Human":
            self.AbilityScoreIncrease = [1, 1, 1, 1, 1, 1]
            self.Speed = 30
            self.Size = "Medium"
            self.Languages = ["Common"]
        elif RaceName == "Elf":
            pass
        else:
            self.AbilityScoreIncrease = [0, 0, 0, 0, 0, 0]
            self.Speed = 30
            self.Size = "Medium"
            self.Languages = ["Common"]

class SubraceTraits:
    pass 


# Jhon = Character(Name, Experience, RaceTraits, ClassTraits, Abilities, Background, Inventory, Alignment)
# Jhon = Character("Jhon", 0, "Human", "Fighter", [15, 14, 13, 12, 10, 8], "Soldier", Inventory, "CG")

Jhon = Character(Resources(20, 15, 2, 0), [15, 14, 13, 12, 10, 8], "Human")
print("Jhon's hp are " + str(Jhon.RacialTraits.Speed))
print("Jhon's Strength value is " + str(Jhon.abilities.strength.value))
print("Jhon's Strength modifier is " + str(Jhon.abilities.strength.modifier))