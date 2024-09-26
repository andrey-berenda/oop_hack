class Person:
    def __init__(self, name, hp=100, damage=10, protection=5):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.protection = protection

    def set_things(self):
        pass

def atack_score(player_one, player_two):
    while player_one.hp > 0 or player_two.hp > 0:
        player_one.hp = player_one.hp - (player_two.damage - (player_two.damage*player_one.protection/100))
        player_two.hp = player_two.hp - (player_one.damage - (player_one.damage*player_two.protection/100))
        print(f'У {player_one.name} HP = {player_one.hp}\n У {player_two.name} HP = {player_two.hp}')
        if player_one.hp <= 0:
            print(f'Победил {player_two.name}')
            break
        if player_two.hp <= 0:
            print(f'Победил {player_one.name}')
            break


#class Thing:
#    def __init__(self, name, increase_hp=0, increase_damage=0, increase_protection=0):
#        self.name = name
#        self.increase_hp = increase_hp
#        self.increase_damage = increase_damage
#        self.increase_protection = increase_protection


class Warrior(Person):
    def __init_(self, name, hp, damage, protection):
        super().__init__(hp, protection, name)
        self.damage = damage * 2


class Paladin(Person):
    def __init__(self, name, hp, damage, protection):
        super().__init__(name, damage)
        self.hp = hp * 2
        self.protection = protection * 2

def main():
    # Things
#    vanguard = Thing(name='Vanguard', increase_protection=5)
#    crystalis = Thing(name='Crystalis', increase_damage=10)
#    sword = Thing(name='Sword', increase_damage=15)
#    armor = Thing(name='Armor', increase_protection=20)

    # Warriors
    slark = Warrior(name='Slark', damage=20)

    # Paladins
    mars = Paladin(name='Mars', hp=100, protection=10, damage=10)

    atack_score(slark, mars)

if __name__ == "__main__":
    main()
   
