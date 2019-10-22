import random

"""Classes of All Items"""


class Item:
    """Main Class for Items to inherit from"""
    def __init__(self, name, price):
        self.name = name
        self.price = price



class Weapon(Item):
    """The Weapon Class"""

    def __init__(self, name,  price ,min_dmg, max_dmg):
        super().__init__(name, price )

        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def __str__(self):
        return "{0} DMG: {1} - {2} Price:{3}".format(self.name, self.min_dmg, self.max_dmg, self.price)

    def dmg_roll(self):
        return random.randint(self.min_dmg, self.max_dmg)


class Shield(Item):
    """The Shield Class"""

    def __init__(self, name, price, block_value):
        super().__init__(name, price)

        self.block_value = block_value

    def __str__(self):
        return "{0} Block Value: {1} Price:{2}".format(self.name, self.block_value, self.price)

    def block_roll(self):
        rand_decision = random.randint(0, 1)
        if rand_decision == 1:
            return self.block_value
        return 0


class Armor(Item):
    """The Armor Class"""

    def __init__(self, name, price, armor_value ):
        super().__init__(name, price)

        self.armor_value = armor_value

    def __str__(self):
        return "{0} Armor Value: {1} Price:{2}".format(self.name, self.armor_value, self.price)


class Potion(Item):
    """The Potion Class"""

    def __init__(self, name, price, heal_value):
        super().__init__(name, price)
        self.heal_value = heal_value

    def __str__(self):
        return "{0} Heal Value: {1} Price:{2}".format(self.name, self.heal_value, self.price)


