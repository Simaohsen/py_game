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


class Simple_Enemy(Enemy):

    def __init__(self):
        self.name = "Simple Enemy"
        super().__init__(10, 1, 3, 2)


class Medium_Enemy(Enemy):

    def __init__(self):
        self.name = "Medium Enemy"
        super().__init__(20, 4, 8, 5)


class Hard_Enemy(Enemy):

    def __init__(self):
        self.name = "Hard Enemy"
        super().__init__(30, 6, 10, 10)


class Endboss(Enemy):

    def __init__(self):
        self.name = "Endboss"
        super().__init__(45, 10, 15, 100)