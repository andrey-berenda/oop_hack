from random import choice, randint


names_of_things = [
    'Эбонитовый посох с рунами',
    'Кольчуга из чешуи дракона',
    'Плащ теней',
    'Золотой амулет с сапфиром',
    'Боевые рукавицы гладиатора',
    'Шлем черного стража',
    'Серебряный медальон предвидения',
    'Мантия звездного мага',
    'Перчатки из кожи василиска',
    'Аметистовый жезл силы',
    'Куртка из волчьей шкуры',
    'Двуручный меч рыцаря',
    'Обсидиановый кинжал',
    'Сапоги путешественника',
    'Щит с гербом единорога',
    'Ожерелье древних духов',
    'Бронзовая булава',
    'Пояс могущества',
    'Перстень истинного зрения',
    'Латные наручи паладина',
    'Костяной лук охотника',
    'Шипастые наплечники',
    'Глиняный амулет защиты',
    'Роговой шлем берсерка',
    'Кожаные портки разбойника',
    'Топор дварфийского кузнеца',
    'Наручи из драконьей кости',
    'Маска демона',
    'Железные поножи',
    'Капюшон убийцы',
    'Рубиновое ожерелье власти',
    'Дубинка тролля',
    'Плащ зимнего волка',
    'Серебряная серьга колдуна',
    'Шелковая туника мага',
    'Стальной наручь лучника',
    'Перчатки мастера клинка',
    'Кольцо с черным алмазом',
    'Посох древнего друида',
    'Кожаный картуз искателя',
]
names_of_persons = [
    'Артарион',
    'Кайрос Ветрокрылый',
    'Лираэль Звёздная',
    'Громгард Железнобокий',
    'Серафинна Ночная Тень',
    'Торвин Огненный Клинок',
    'Элиана Серебролист',
    'Моргантир Чёрный Пламень',
    'Финн Дикий Ветер',
    'Валандра Лунная Прядь',
]


class Thing:
    def __init__(self):
        self.name = choice(names_of_things)
        self.protection_percent = self.define_protection_percent()
        self.attack = self.define_attack()
        self.health = self.define_health()

    def define_protection_percent(self):
        return randint(1, 10) / 100

    def define_attack(self):
        return randint(1, 10)

    def define_health(self):
        return randint(1, 10)


class Person:
    def __init__(
        self,
        name=None,
        base_health=100,
        base_attack=10,
        base_armor=0.01,
        inventory=None,
        damage=0,
        additionally_protection=0
    ):
        self.name = name or choice(names_of_persons)
        self.all_attack = base_attack
        self.all_armor = base_armor
        self.health = base_health
        self.inventory = inventory or []
        self.additionally_protection = additionally_protection

    def set_things(self, things):
        number_of_things = randint(1, 4)
        for _ in range(number_of_things):
            thing = choice(things)
            self.inventory.append(thing)
            self.health += thing.health
            self.all_armor *= (1 + thing.protection_percent)
            self.all_attack += thing.attack

    def take_damage(self, damage):
        actual_damage = damage * (1 - self.all_armor)
        self.health -= max(actual_damage, 0)

    def all_protection(self):
        self.all_armor += self.additionally_protection


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.all_armor *= 2
        self.health *= 2


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.all_attack *= 2


def create_things():
    things = [Thing() for _ in range(41)]
    return sorted(things, key=lambda x: x.protection_percent, reverse=True)


def create_personages():
    classes = [Paladin, Warrior]
    return [choice(classes)() for _ in range(10)]


def main():
    things = create_things()
    personages = create_personages()

    for personage in personages:
        personage.set_things(things)

    while len(personages) > 1:
        attacker = choice(personages)
        defender = choice([p for p in personages if p != attacker])

        damage = max(attacker.all_attack * (1 - defender.all_armor), 0)
        defender.take_damage(damage)

        print(f'{attacker.name} атакует {defender.name},'
              f'нанося {damage:.1f} урона!')
        print(f'У {defender.name} осталось {defender.health:.1f} HP')

        if defender.health <= 0:
            print(f'{defender.name} погиб!')
            personages.remove(defender)

    print(f'{personages[0].name} победил!')


if __name__ == '__main__':
    main()
