import random


class Thing:
    def __init__(self, name, defense_percent, attack_power, health_point):
        self.name = name
        self.defense_percent = defense_percent
        self.attack_power = attack_power
        self.health_point = health_point


def create_things():
    things = []
    for thing in range(20):
        name = f'какая-то вещь {thing}'
        defense_percent = random.randint(0, 10) / 100
        attack_power = random.randint(0, 20)
        health_point = random.randint(0, 100)
        things.append(Thing(name, defense_percent, attack_power, health_point))
    return things


class Person:
    def __init__(self):
        self.health_point = 100
        self.attack_power = 100
        self.defense = 1
        self.things = []

    def set_things(self, things):
        self.things = things
        for thing in things:
            self.defense += thing.defense_percent

    def calculate_health(self, attack_power):
        self.health_point -= attack_power - (attack_power / 100 * self.defense)


class Paladin(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health_point *= 2
        self.defense *= 2


class Warrior(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.attack_power *= 2


def create_warriors():
    warriors = []
    for person in range(2):
        names = ['war1', 'war2']
        war = Warrior(name=names[0])
        warriors.append(war)
        del names[0]
    return warriors


def create_palladins():
    palladins = []
    for person in range(2):
        names = ['pal1', 'pal2']
        war = Paladin(name=names[0])
        palladins.append(war)
        del names[0]
    return palladins


things = create_things()


fighters = create_warriors() + create_palladins()

for fighter in fighters:
    num_things = random.randint(1, 4)
    fighter.set_things(random.sample(things, num_things))


while len(fighters) != 1:
    attacker = fighters[random.randint(0, len(fighters) - 1)]
    while True:
        target = fighters[random.randint(0, len(fighters) - 1)]
        if target != attacker:
            break
    target.calculate_health(attacker.attack_power)
    if target.health_point <= 0:
        print(f'{target.name} умер')
        fighters.remove(target)
        continue
    print(
        f'{attacker.name} атаковал {target.name} силой {attacker.attack_power}'
    )
print(f'{fighters.pop().name} победитель')
