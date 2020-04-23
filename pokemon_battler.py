import random
from random import randint
from pick import pick

class Pokemon:

    def __init__(self, name, level, type, maximum_health, current_health,
    current_status):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.current_status = current_status

    def attack(self):
        if self.type == self.type:
            self.current_health = self.maximum_health
            self.current_health -= self.level
        elif self.type == self.type:
            self.current_health = self.maximum_health
            self.current_health -= self.level

    def lose_health(self):
        print('{name} now has {current_health} health!'.format(name = self.name,
        current_health = self.current_health))
    def gain_health(self):
        print('{name} now has {current_health} health!'.format(name = self.name,
        current_health = self.current_health))
    def knock_out(self):
        print('{name} has been knocked out!'.format(name = self.name))
    def revive(self):
        print('{name} has been revived!'.format(name = self.name))


class Trainer:
    def __init__(self, name, fighting_pokemon, potions, pokemon_inventory):
        self.name = name
        self.fighting_pokemon = fighting_pokemon
        self.potions = potions
        self.pokemon_inventory = pokemon_inventory

    def __repr__(self):
        return """Opponent: {name}
Pokemon: {active_pokemon}
Items Available: {potions} Potions
Available Pokemon: {pokemon_inventory}\n""".format(name=self.name,
active_pokemon=self.fighting_pokemon, potions
        =self.potions, pokemon_inventory=self.pokemon_inventory)


#different pokemon
charmander = Pokemon('Charmander', 10, 'Fire', 100, 100, 'Alert')
squirtle = Pokemon('Squirtle', 10, 'Water', 100, 100, 'Alert')
pikachu = Pokemon('Pikachu', 10, 'Electric', 100, 100, 'Alert')
bulbasaur = Pokemon('Bulbasaur', 10, 'Grass', 100, 100, 'Alert')
psyduck = Pokemon('Psyduck', 10, 'Pychic', 100, 100, 'Alert')
beedrill = Pokemon('Beedrill', 10, 'Bug', 100, 100, 'Alert')
pokemon_list = [charmander, squirtle, pikachu, bulbasaur, psyduck, beedrill]

trainer_names = ['Brock', 'Misty', 'Ash', 'Gary', 'Jessie', 'James']

#Random opponant generator
opponent_team = []
opponent_pokemon = random.choice(pokemon_list).name
teams = random.sample(pokemon_list, random.randint(1,6))
for team in teams:
    if team.name == opponent_pokemon: #player's pokemon not in unused inventory
        continue
    else:
        opponent_team.append(team.name)
trainer_two = Trainer(random.choice(trainer_names),
opponent_pokemon, randint(0,10), player_team)

print(trainer_two)
