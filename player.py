import time
import inventory


class Player:

    """The Player Class"""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = inventory.Inventory()
        print("Player {0} created. \nHealth:{1}".format(self.name, self.health))

    def fight(self, Enemy):
        while self.health > 0 and Enemy.health > 0:
            player_turn_dmg = self.inventory.weapon.dmg_roll()
            Enemy.health -= player_turn_dmg
            print("{0} deals {1} DMG! {2} has {3} Health left!".format(self.name, player_turn_dmg, Enemy.name, Enemy.health))
            if Enemy.health <= 0:
                print("You Win!")
                return True

            time.sleep(2)
            enemy_turn_dmg = Enemy.dmg_roll() - self.inventory.armor.armor_value - self.inventory.shield.block_roll()
            if enemy_turn_dmg > 0:
                self.health -= enemy_turn_dmg
                print("{0} deals {1} DMG! {2} has {3} Health left!".format(Enemy.name, enemy_turn_dmg, self.name, self.health))
            else:
                print("{0} deals no DMG! {1} has still {2} Health left!".format(Enemy.name, self.name, self.health))
            if self.health <= 0:
                print("You lose!")
                return False
            time.sleep(2)

    def set_item(self, item):
        self.inventory.set_item(item)

    def print_inventory(self):
        for item in self.inventory.get_inventory():
            print(item)