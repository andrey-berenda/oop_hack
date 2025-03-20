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
        self.attack = self.define_attack
        self.health = self.define_health

    def define_protection_percent(self):
        self.protection_percent = randint(1, 10) / 100

    def define_attack(self):
        self.attack = randint(1, 10)

    def define_health(self):
        self.health = randint(1, 10)


class Person:
    def __init__(
        self,
        name=None,
        base_health=100,
        base_attack=10,
        base_armor=0.01,
        inventory=None,
        damage=None,
        additionally_protection=None,
    ):
        self.name = name
        self.base_health = base_health
        self.base_attack = base_attack
        self.base_armor = base_armor
        self.all_attack = self.take_damage(damage or 0)
        self.all_armor = self.all_protection(additionally_protection or 0)
        self.inventory = self.set_things(inventory or [])
        self.additionally_protection = additionally_protection or 0

    def set_things(self, things):
        number_of_things = randint(1, 4)
        for _ in range(number_of_things + 1):
            thing = choice(things)
            self.health += thing.health
            self.all_armor *= thing.protection_percent
            self.all_attack += thing.attack

    def take_damage(self, damage):
        self.health -= damage - damage * self.all_armor

    def set_things(self, inventory):
        pass

    def take_damage(self, damage):
        self.base_attack = self.base_attack + damage

    def all_protection(self, additionally_protection):
        self.base_armor = self.base_armor + additionally_protection


class Paladin(Person):
    def __init__(self):
        super().__init__(
            choice(names_of_persons),
        )
        self.armor = self.base_armor * 2
        self.health = self.base_health * 2


class Warrior(Person):
    def __init__(self):
        super().__init__(
            choice(names_of_persons),
        )
        self.attack = self.base_attack * 2


def create_things():
    things = []

    for _ in range(40):
        things.append(Thing())
    print(vars(things[0]))
    return things.sort(key=lambda x: x.protection_percent)


def create_personages():
    classes = [Paladin, Warrior]
    personages = []
    for _ in range(10):
        RandomClass = choice(classes)
        personages.append(RandomClass())
    return personages


def main():
    things = create_things()
    personages = create_personages()
    for pesonage in personages:
        pesonage.set_things(things)
    while True:
        attacker = choice(personages)
        others = [person for person in personages if person != attacker]
        defender = choice(others)
        defender.take_damage(attacker.all_attack)
        if defender.health <= 0:
            personages.remove(defender)
        if len(personages) == 1:
            print(f'{personages[0].name} победил!')
            break


if __name__ == '__main__':
    main()
