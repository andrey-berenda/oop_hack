#Персонаж: class Person Класс, содержащий в себе следующие параметры:

#Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты. Параметры передаются через конструктор;
#метод, принимающий на вход список вещей set_things(things);
#метод вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;
#Паладин: class Paladin Класс наследуется от персонажа, при этом количество присвоенных жизней и процент защиты умножается на 2 в конструкторе;
#Воин: class Warrior Класс наследуется от персонажа, при этом атака умножается на 2 в конструкторе.


class Person():

    def __init__(self, name, hp, base_attack, base_defense):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defense = base_defense

    def set_things(self, things):
        self.things = things

    def minus_hp(self, attack):
        return self.hp - self.attack

    

#hobbit = Person("Фродо", 10, 2, 0)
#hobbit.set_things(['Жало'])

#print(hobbit.things)