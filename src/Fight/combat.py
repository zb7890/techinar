from random import randint


class Fighter:
    """This class represents a generic fighter character."""

    def __init__(self, name, health, defense, power, damage,superpower,superpowerdamage):
        """Initialize the fighter with the given attributes."""
        self.name = name
        self.health = health
        self.defense = defense
        self.power = power
        self.damage = damage
        self.superpower=superpower
        self.superpowerdamage=superpowerdamage

    def alive(self):
        """Determine if the fighter is alive."""

        return self.health > 0


    def attack(self, opponent):
        """Have the fighter attack an opponent."""

        roll = randint(1, 20)
        if roll + self.power - opponent.defense > 12:
            print(f"{self.name} hits {opponent.name} for {self.damage} points")
            opponent.wound(self.damage)
            if not opponent.alive():
                 print(f"{self.name} won!")
        else:
            print(f"{self.name} missed.")    
        if randint(1,20)>10:
            print(f"{self.name} hits {opponent.name} for {self.superpowerdamage} points with {self.superpower}!!!")
            opponent.wound(self.damage)
            if not opponent.alive():
                print(f"{self.name} won!")


    def wound(self, amount):
        """Apply damage to the fighter."""

        self.health -= amount
        if not self.alive():
            print(f"{self.name} died.")


    def print_status(self):
        """Print the current status of the fighter."""
        print(f"{self.name} has {self.health} health.")


f1 = Fighter(name="Newcomb", health=10, defense=4, power=5, damage=2,superpower="math quiz",superpowerdamage=6)
f2 = Fighter(name="Aneesh", health=11, defense=4, power=3, damage=2,superpower="Curry Bomb",superpowerdamage=7)
f3= Fighter(name="Matthew",health=9,defense=3,power=4,damage=3,superpower="Super punch",superpowerdamage=10)
f4= Fighter(name="Kouki",health=9,defense=3,power=4,damage=4,superpower="super kick",superpowerdamage=9)
print(f"{f1.name} vs {f2.name}")
round = 1
while f1.alive() and f2.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f2.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f1.attack(f2)
    if f2.alive():
        answer = input(f"Should {f2.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f2.attack(f1)
    round += 1
round=2
while f3.alive() and f4.alive():
    print(f"\nRound {round}")
    f3.print_status()
    f4.print_status()
    answer = input(f"Should {f3.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f3.attack(f4)
    if f4.alive():
        answer = input(f"Should {f4.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f4.attack(f3)
round=3
if f1.alive() and f3.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f3.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f1.attack(f3)
    if f3.alive():
        answer = input(f"Should {f3.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f3.attack(f1)
round=4
if f1.alive() and f4.alive():
    print(f"\nRound {round}")
    f1.print_status()
    f4.print_status()
    answer = input(f"Should {f1.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f1.attack(f4)
    if f4.alive():
        answer = input(f"Should {f4.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f4.attack(f1)
round=5
if f2.alive() and f3.alive():
    print(f"\nRound {round}")
    f2.print_status()
    f3.print_status()
    answer = input(f"Should {f2.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f2.attack(f3)
    if f3.alive():
        answer = input(f"Should {f3.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f3.attack(f2)
round=6
if f2.alive() and f4.alive():
    print(f"\nRound {round}")
    f2.print_status()
    f4.print_status()
    answer = input(f"Should {f2.name} attack? (Y or N) ")
    if answer.lower() == "y":
        f2.attack(f4)
    if f4.alive():
        answer = input(f"Should {f4.name} attack? (Y or N) ")
        if answer.lower() == "y":
            f4.attack(f2)
    round += 1

print("Fight over.")
