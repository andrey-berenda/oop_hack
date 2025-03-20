from random import randint, shuffle, choice
class Person():

    def __init__(self, name, hp, base_attack, base_defence):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.things = []

    def set_things(self, things):
        self.things.append(things)

    def minus_hp(self, attack):
        return self.hp - attack


ITEM_NAMES = [
"Кольцо Вечности",
"Меч Судьбы",
"Посох Звёздного Света",
"Щит Невидимости",
"Амулет Древних",
"Плащ Теней",
"Браслет Ветра",
"Книга Заклинаний",
"Сапоги Летучего Мыша",
"Чаша Бессмертия",
"Перо Феникса",
"Зеркало Илюзий",
"Кристалл Времени",
"Сфера Элементов",
"Гаечный ключ Миров",
"Лук Лунного Света",
"Кольцо Призывателя",
"Сумка Бесконечности",
"Ожерелье Силы",
"Талисман Защитника",
]

class Thing:
    def __init__(self, name, defence, attack, hp):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hp = hp

class Warrior(Person):
    def __init__(self, name, base_defence, base_attack, hp):
        super().__init__(name, base_defence, base_attack, hp)
        self.base_attack = self.base_attack * 2


class Paladin(Person):
    def __init__(self, name, base_defence, base_attack, hp):
        super().__init__(name, base_defence, base_attack, hp)
        self.hp = self.hp * 2
        self.base_defence = self.base_defence * 2

ring = Thing("Кольцо всевластия", attack=1, defence=2, hp=100)
print(ring.attack)


# Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1). Сортируем по проценту защиты, по возрастанию;

ITEMS_NUMBER = randint(40, 100)

def items_creation():
    items = ([Thing(ITEM_NAMES[randint(0, 19)], randint(0, 10)/100, randint(0, 10), 100) for _ in range(ITEMS_NUMBER)])
    return sorted(items, key=lambda thing: thing.defence)

# for i in items_creation():
#     print(i.name)
#     print(i.defence)

fantasy_characters = [
    "Aelara Stormrider",
    "Thalorin Fireheart",
    "Lyria Moonshadow",
    "Kaelith Duskblade",
    "Eryndor Silverleaf",
    "Seraphina Dawnbringer",
    "Drakthar Ironfist",
    "Isolde Nightwhisper",
    "Fenrir Frostbane",
    "Zephyra Windrider",
    "Morvyn Shadowcloak",
    "Elowen Starweaver",
    "Ragnar Bloodaxe",
    "Sylvaris Greenwarden",
    "Lunara Darkmoon",
    "Tharion Flamecaller",
    "Aurelia Sunspire",
    "Vorian Nightshade",
    "Kaelara Stormforge",
    "Eldrin Lightbringer",
]


# Шаг 2 - создаем произвольно 10 персонажей, кол-во воинов и паладинов произвольно. 
# Имена персонажам тоже рандомные из созданного списка 20 имен. 
# Придумайте своих уникальных персонажей или заставьте сражаться знаменитостей, посмотрим кто сильнее =)

shuffle(fantasy_characters)

def generate_characters():
    fighters =[]
    for character in fantasy_characters[:10]:
        if randint(0, 1):
            fighters.append(Paladin(character, randint(0, 100), randint(0, 100), randint(0, 100)))
        else:
            fighters.append(Warrior(character, randint(0, 100), randint(0, 100), randint(0, 100)))
    return fighters


# for i in generate_characters():
#     print(i.name)

# Шаг 3 - одеваем персонажей рандомными вещами. Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;

characters = generate_characters()
items = items_creation()

def items_allocation(characters, items):
    for character in characters:
        for _ in range(randint(1, 4)):
            item = items.pop()
            character.set_things(item)

#items_allocation(characters, items)
#for i in characters:
    #print(i.name)
    #for name in range(len(i.things)):
        #print((i.things[name].name))


def main():
    for f in range(len(characters) - 1):
        attacker = characters[f]
        defender = characters[f + 1]
        defender.minus_hp(attacker.base_attack)
        

    
if __name__ == '__main__':
    main()