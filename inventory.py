import items


class Inventory:
    """The Inventory Class"""

    def __init__(self):
        self.gold = 0
        self.weapon = items.Weapon("Short Sword", 0, 1, 5)
        self.shield = items.Shield("Wooden Shield", 0, 1)
        self.armor = items.Armor("Leather Scraps", 0, 1)
        self.potion = items.Potion("Healing Potion", 0, 15)
        self.potion_counter = 1

    def add_gold(self, gold_added):
        if gold_added > 0:
            self.gold += gold_added

    def spend_gold(self, gold_spent):
        if self.gold - gold_spent >= 0:
            self.gold -= gold_spent
            return True
        else:
            return False


    def set_item(self, item):
        if (isinstance(item, items.Weapon)):
            self.weapon = item
        elif (isinstance(item, items.Shield)):
            self.shield = item
        elif (isinstance(item, items.Armor)):
            self.armor = item

    def add_potion(self):
        self.potion_counter +=1

    def get_inventory(self):
        return [self.weapon, self.shield, self.armor]

    def print_inventory(self, player):
        for item in self.get_inventory():
            print(item)
        print(str(self.gold) + " Gold")
        print("Health: " + str(player.health))
        print("Healing Potions: " + str(self.potion_counter))