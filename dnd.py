# A "simple" turn-based combat simulation for a Dungeons & Dragons-like game made to learn Python.
import random
class Mortal:
    def __init__(self, name, armor_class, health, dodge_chance, Crit_chance):
        self.name = name
        self.armorClass = armor_class
        self.health = health
        self.max_health = health
        self.health_potion_uses = 3
        self.dodge_chance = dodge_chance
        self.Crit_chance = Crit_chance

    def is_alive(self):
        return self.health > 0
    
    def get_health_state(self):
        return f"({self.health}/{self.max_health})"
    
    def receive_attack(self, attack_roll, damage_roll):
        if attack_roll <= self.armorClass:
            print(self.name, "blocked your attack roll of", attack_roll)
        elif attack_roll <= 20 and (dodge_roll := random.randint(1, 100)) <= self.dodge_chance:
            print(f"{self.name} dodged the attack!")
            return
        else:
            self.health = self.health - damage_roll
            print(self.name, "took", damage_roll, "damage", self.get_health_state())
            if attack_roll == 20:
                print(self.name, "took", damage_roll, "extra critical hit damage", self.get_health_state())
                self.health = self.health - damage_roll
            if not self.is_alive():
                print(self.name, "died")

    def attack(self, target):
        if not self.is_alive():
            print(self.name, "is dead and cannot attack.")
            return

        attack_roll = roll_d20()
        damage_roll = roll_d10()
        target.receive_attack(attack_roll, damage_roll)
        print(self.name, "attacks", target.name, "with a roll of", attack_roll)
    

    def health_potion(self):
        if self.is_alive() and self.health <= (1/2 * self.max_health):
            if self.health_potion_uses > 0:
                self.health += random.randint(1, 4) + 2
                self.health_potion_uses -= 1
                print(self.name, "drank a health potion and restored health", self.get_health_state())
            else:
                print(self.name, "has no health potions left")


# function to roll a d20
def roll_d20():
    return random.randint(1, 20)
def roll_d10():
    return random.randint(1, 10)

# Super cool intro cinamatics and palyer name 
print("PLACE HOLDER -- something cool setting up a story -- ending with a charecter selection")
player_name = input("Enter your hero's name: ")

# Rejects boring ahh titles
generic_titles = {
    "The Bold", "The Brave", "The Cunning", "The Fierce", "The Great",
    "The Just", "The Mighty", "The Swift", "The Valiant", "The Wise", "The Kind"
}

# Ask for title until it's not too generic
print(f"Greetings {player_name}, as every great adventurer before you has figured out; "
        f"the only difference between a hero and an NPC is a powerful sounding title.\n")
while True:
    player_title = input(
        f"So {player_name}, what shall your title be? "
    ).title()

    if player_title in generic_titles:
        print("Boring, do better!\n")
    else:
        print(f"Ahh... '{player_name} {player_title}' now **that** sounds like the name of a true legend!")
        break

# order of stats for easy reference (armor_class, health, dodge_chance, Crit_chance)
enemies = [
    Mortal("Goblin Archer 1", 12, 12, 3, 0),
    Mortal("Goblin Archer 2", 12, 12, 3, 0),
    Mortal("Goblin Archer 3", 12, 12, 3, 0),
    Mortal("Goblin Boss", 14, 30, 20, 0) 
]

# order of stats for easy reference (armor_class, health, dodge_chance, Crit_chance)
players = [
    Mortal("Barbarian", 16, 40, 5, 0),
    Mortal("Wizard", 13, 25, 1, 0),
    Mortal("Druid", 13, 25, 1, 0),
    Mortal("Paladin", 13, 25, 1, 0),
    Mortal("Ranger", 13, 25, 20, 0),
    Mortal("Rogue", 13, 25, 40, 0),
    Mortal("Cleric", 13, 25, 1, 0),
    Mortal("Fighter", 16, 25, 25, 0),
    Mortal("Bard", 13, 25, 15, 0)
]

# Show available classes once at the start
print("\nAvailable classes:")
for cls in players:
    print(f"- {cls.name}")

# Ask player to choose a class by name
while True:
    chosen_class_name = input(
        f"\nSo, {player_name} {player_title}, what class are you? "
    ).strip().title()

    chosen_class = next((cls for cls in players if cls.name == chosen_class_name), None)

    if chosen_class:
        break
    else:
        print("That's not one of the available classes. Try again!")
        print("Available classes:", ', '.join(cls.name for cls in players))  

#function to see who wins
while len(enemies) > 0 and len(players) > 0:

    for player in players:
        if len (enemies) == 0:
            break
        enemy = random.choice(enemies)

        player.attack(enemy)
        if not enemy.is_alive():
            enemies.remove(enemy)

    for enemy in enemies:
        if len(players) == 0:
            break
        player = random.choice(players)

        enemy.attack(player)
        if not player.is_alive():
            players.remove(player)

if len(players) > 0:
    print("Players win!")
else:
    print("Monsters win!")
