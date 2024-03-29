import items



class Shop:
    """The Shop Class"""

    def __init__(self):

        self.itemlist = [items.Weapon("Better Sword", 2, 2, 7), items.Armor("Better Armor", 2, 2), items.Shield("Better Shield", 2, 2),items.Weapon("Ultra Sword", 8, 10, 15), items.Armor("Ultra Armor", 8, 8), items.Shield("Ultra Shield",8, 10) ]
        self.potion = items.Potion("Healing Potion", 1, 10)



    def return_item(self, item):
        return item

    def show_shop_prompt(self, player):

        print("Welcome to the Shop. What do you want to buy?\n[1]Items\n[2]Potions\n[X]Go Back")
        player_input = input("What do you choose?:").lower()
        if player_input == "1":
            self.show_items_prompt(player)
        elif player_input == "2":
            self.show_potions_prompt(player)
        elif player_input == "x":
            return False


    def show_items_prompt(self, player):
        print("Choose an Item:")
        for item in self.itemlist:
            print("[{0}]".format(str(self.itemlist.index(item)+1))+str(item))

        print("[X]Go Back")
        player_input = input("Which Item do you want?:")

        if not player_input == "x":
            player_input_int = int(player_input)-1
        if player_input == "x":
            self.show_shop_prompt(player)

        elif self.get_item(player_input_int).price <= player.inventory.gold:
            player.set_item(self.get_item(player_input_int))
            player.spend_gold(self.get_item(player_input_int).price)


    def show_potions_prompt(self, player):
        print("Want to buy a Healing Potion?[Y]es / [N]o ?")
        player_input = input("Your Choice: ").lower()
        if player_input == "y":
            if self.potion.price <= player.inventory.gold:
                player.inventory.spend_gold(self.potion.price)
                player.add_potion()
            else:
                print("Not enough Gold!")




    def get_item(self, input):
        return self.itemlist[input]

