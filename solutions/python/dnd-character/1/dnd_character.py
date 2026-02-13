class Character:
    def __init__(self):
        self.strength = ability()
        self.dexterity = ability()
        self.constitution = ability()
        self.intelligence = ability()
        self.wisdom = ability()
        self.charisma = ability()

        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        return ability()

import random as r

def ability():
    rolls = [r.randint(1, 6) for _ in range(4)]
    return sum(rolls) - min(rolls)

def modifier(value):
    return (value - 10)//2