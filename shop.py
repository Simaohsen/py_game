import items



class Shop:
    """The Shop Class"""

    def __init__(self):

        self.itemlist = [items.Weapon("Better Sword", 2, 3, 8), items.Armor("Better Armor", 2, 2), items.Shield("Better Shield", 2, 2)]
        self.potionlist = [items.Potion("Healing Potion", 2, 10)]



    def return_item(self, item):
        return item

    def show_shop_prompt(self, player):

        print("Welcome to the Shop. What do you want to buy?\n[1]Items\n[2]Potions\n[X]Go Back")
        player_input = input("What do you choose?:").lower()
        if player_input == "1":
            self.show_items_prompt(player)
        elif player_input == "2":
            pass
        elif player_input == "x":
            return False


    def show_items_prompt(self, player):
        print("Choose an Item:")
        for item in self.itemlist:
            print("[{0}]".format(str(self.itemlist.index(item)+1))+str(item))

        print("[X]Go Back")
        player_input = int(input("Which Item do you want?:"))-1
        if player_input == "x":
            self.show_shop_prompt(player)
        elif self.get_item(player_input).price<= player.inventory.gold:
            player.set_item(self.get_item(player_input))
            player.spend_gold(self.get_item(player_input).price)



    def get_item(self, input):
        return self.itemlist[input]

