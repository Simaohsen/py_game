import random


class Enemy:
    """The Enemy Class"""
    def __init__(self, health, min_dmg, max_dmg, loot):
        self.name = "Enemy"
        self.health = health
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.loot = loot

    def dmg_roll(self):

        return random.randint(self.min_dmg, self.max_dmg)