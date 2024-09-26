import random


class Person:
    def __init__(self):
        self.health_point = 100
        self.attack_power = 100
        self.defense = 1

    def set_things(self, things):
        self.things = things

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
    names = [
        'war1',
        'war2',
        'war3',
        'war4',
        'war5',
        'war6',
        'war7',
        'war8',
        'war9',
        'war10',
    ]
    for person in range(10):
        war = Warrior(name=names[0])
        warriors.append(war)
        names.remove(names[0])
    return warriors


def create_palladins():
    palladins = []
    names = [
        'pal1',
        'pal2',
        'pal3',
        'pal4',
        'pal5',
        'pal6',
        'pal7',
        'pal8',
        'pal9',
        'pal10',
    ]
    for person in range(10):
        war = Paladin(name=names[0])
        palladins.append(war)
        names.remove(names[0])
    return palladins


fighters = create_warriors() + create_palladins()
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


def main():
    pass


if __name__ == '__main__':
    pass
