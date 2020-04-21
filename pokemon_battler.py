import random

class Pokemon:

    def __init__(self, name, level, type, maximum_health, current_health, current_status):
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
        print('{name} now has {current_health} health!'.format(name = self.name, current_health = self.current_health))
    def gain_health(self):
        print('{name} now has {current_health} health!'.format(name = self.name, current_health = self.current_health))
    def knock_out(self):
        print('{name} has been knocked out!'.format(name = self.name))
    def revive(self):
        print('{name} has been revived!'.format(name = self.name))

#different pokemon
charmander = Pokemon('Charmander', 10, 'Fire', 100, 100, 'Alert')
squirtle = Pokemon('Squirtle', 10, 'Water', 100, 100, 'Alert')
pikachu = Pokemon('Pikachu', 10, 'Electric', 100, 100, 'Alert')
bulbasaur = Pokemon('Bulbasaur', 10, 'Grass', 100, 100, 'Alert')
psyduck = Pokemon('Psyduck', 10, 'Pychic', 100, 100, 'Alert')
beedrill = Pokemon('Beedrill', 10, 'Bug', 100, 100, 'Alert')

class Trainer:
    def __init__(self, name, pokemon_list, potion, active_pokemon):
        self.name = name
        self.pokemon_list = pokemon_list
        self.potion = potion
        self.active_pokemon = active_pokemon

    def repr(self):
        self.name = random.choice(trainer_names)
        return "{name} will be the first challenger".format(name=self.name)

trainer_names = ['Brock', 'Misty', 'Ash', 'Gary', 'Jessie', 'James']
trainer_one = Trainer()
print(trainer_one)
