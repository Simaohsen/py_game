from shop import Shop
from fight import Fight
from enemy import Enemy

class City:

    def __init__(self, player, world):
        self.player = player
        self.shop = Shop()
        self.world = world
        self.arena_fights = 0

    def print_city_menu(self):
        print("Your Turn! Choose what you want to do!\n[1]To fight in the Arena!\n[2]To enter the Shop\n[3]To show your "
              "Inventory\n[4]To venture in to the World!\n[X]To quit the Game!")

    def arena_fight(self):

        self.arena_fights += 1

        if 5 <= self.arena_fights < 10:
            return Fight(self.player, Enemy(20,2, 5, 3)).fight()

        elif self.arena_fights >= 10:
            return Fight(self.player, Enemy(25, 4, 8, 7)).fight()

        return Fight(self.player, Enemy(15,1,3,1)).fight()

    def enter_shop(self):
        in_shop = True
        while in_shop:
            in_shop = self.shop.show_shop_prompt(self.player)

    def enter_city(self):

        player_alive = True
        while player_alive:
            self.print_city_menu()

            player_input = str(input("What do you Choose?")).lower()

            if player_input == "1":
                player_alive = self.arena_fight()

            elif player_input == "2":
                self.enter_shop()

            elif player_input == "3":
                self.player.go_to_inventory(self.player)

            elif player_input == "4":
                player_alive = self.world.run_world()

            elif player_input == "x":
                return False

        return False


