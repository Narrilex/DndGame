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
2-базис: у персонажа есть класс, класс даёт начальное хп.
"""

# Блок сборной сущности (токен, персонаж, монстр, непись)

class Token:
    def __init__(self):
        self.resources = Resources(10, 10, 0, 0)
        self.abilities = Abilities(10, 10, 10, 10, 10, 10)
    

class Character(Token):
    def __init__(self, AbilityValues, RaceName, ClassName):
        
        self.race_name = RaceName
        self.racial_traits = RacialTraits(RaceName)
       
        self.resources = Resources
        self.abilities = Abilities(AbilityValues, self.racial_traits.AbilityScoreIncrease)
       
        self.class_name = ClassName
        self.class_traits = ClassTraits(ClassName)

        #Пока ресурсы расположим тут
        self.max_hp = Resource("max_HP", self.class_traits.hp_1lvl + self.abilities.constitution.modifier)
        self.xp = Resource("xp", 0)
        self.pb = 2
        self.ac = 10 + self.abilities.dexterity.modifier


        #Блок прописанных значений характеристик самому классу персонажа, чтобы не долбиться в характеристики через класс Abilities 
        self.strength_value = self.abilities.strength.value
        self.strength_modifier = self.abilities.strength.modifier

        self.dexterity_value = self.abilities.dexterity.value
        self.dexterity_modifier = self.abilities.dexterity.modifier

        self.constitution_value = self.abilities.constitution.value
        self.constitution_modifier = self.abilities.constitution.modifier

        self.intelligence_value = self.abilities.intelligence.value
        self.intelligence_modifier = self.abilities.intelligence.modifier

        self.wisdom_value = self.abilities.wisdom.value
        self.wisdom_modifier = self.abilities.wisdom.modifier

        self.charisma_value = self.abilities.charisma.value
        self.charisma_modifier = self.abilities.charisma.modifier
        #####################################################################

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
            self.AbilityScoreIncrease = (0, 0, 0, 0, 0, 0)
            self.Speed = 30
            self.Size = "Medium"
            self.Languages = ["Common"]

class SubraceTraits:
    pass

# Блок классовые трейты

class ClassTraits:
    def __init__(self, ClassName) -> None:
        if ClassName == "Fighter":
            self.hp_1lvl = 10
            self.HDice = 10
            self.HDice_amount = 1
            self.hp_per_lvl = 10
            self.hp_per_lvl_average = 6

            # Proficiencies блок
            #Armor: All armor, shields
            #Weapons: Simple weapons, martial weapons
            #Tools: None
            #Saving Throws: Strength, Constitution
            #Skills: Choose two skills from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival
            #Standart Fighter Equipment

            
        elif ClassName == "Rogue":
            self.hp_1lvl = 8
            self.HDice = 8
            self.HDice_amount = 1
            self.hp_per_lvl = 8
            self.hp_per_lvl_average = 5
        elif ClassName == "Cleric":
            self.hp_1lvl = 8
            self.HDice = 8
            self.HDice_amount = 1
            self.hp_per_lvl = 8
            self.hp_per_lvl_average = 5
        elif ClassName == "Wizard":
            self.hp_1lvl = 6
            self.HDice = 6
            self.HDice_amount = 1
            self.hp_per_lvl = 6
            self.hp_per_lvl_average = 4
        else:
            pass

class ArchetypeTraits:
    pass 



# Jhon = Character(Name, Experience, RaceTraits, ClassTraits, Abilities, Background, Inventory, Alignment)
# Jhon = Character("Jhon", 0, "Human", "Fighter", [15, 14, 13, 12, 10, 8], "Soldier", Inventory, "CG")

Jhon = Character([15, 14, 13, 12, 10, 8], "Human", "Fighter")

print("Jhon's hp are " + str(Jhon.max_hp))
print("Jhon's ac is " + str(Jhon.ac))

print("Jhon's Strength value is " + str(Jhon.abilities.strength.value))
print("Jhon's Strength modifier is " + str(Jhon.abilities.strength.modifier))

print("Jhon's Wisdom value is " + str(Jhon.wisdom_value))
print("Jhon's Wisdom modifier is " + str(Jhon.wisdom_modifier))

print("Jhon's HDice is " + str(Jhon.class_traits.HDice_amount) + "d" + str(Jhon.class_traits.HDice))