#TODO: Add easy World Class
from fight import Fight


class World_Tile:
    """World Tile Class to add into the World Grid"""

    def __init__(self, enemy, last_flag):
        self.bool = True
        self.cleared_flag = False
        self.enemy = enemy
        self.last_tile = last_flag



    def show_tile_prompt(self):
        if self.cleared_flag == False:
            print("You Enter Tile. An Enemy awaits you. Get ready to fight {0} to the death!".format(self.enemy.name))
            print("What do you want to do? [F]ight or Flee to the [C]ity?")

        else:
            print("You already visited this tile. The Enemy is dead!")
            print("What do you want to do? [G]o Further or Return to the [C]ity?")




    def show_win_prompt(self):
        #TODO: Add win prompt Method
        """Shown after """

    def tile_cleared(self):
        self.cleared_flag = True


class World:

    def __init__(self, player, tiles):
        self.tiles = tiles
        self.player = player
        self.player_position = 0



    def enter_tile(self, tile):
        tile.show_tile_prompt()
        player_input = input("What do you Choose?:").lower()
        if player_input == "f":
            if self.world_fight(self.player, tile.enemy):
                tile.tile_cleared()
                if not tile.last_tile:
                    self.player_position += 1

                if tile.last_tile:
                    self.player_position = 0
                return True

            else:
                return False

        if player_input == "g":
            if not tile.last_tile:
                self.player_position += 1
            return True



    def world_fight(self,player, enemy):
        return Fight(player, enemy).fight()


    def show_world_prompt(self):

        print("You are venturing through the world! You are at Position {0}".format(self.player_position))
        print("What do you want to do? [E]nter the tile or Return to the [C]ity?")





    def run_world(self):
        game_on = True
        player_alive = True
        world_cleared = False

        while game_on:
            if world_cleared:
                print("You Cleared the Forest!")
                game_on = False

            if not player_alive:
                print("You are dead. Game over! You Lost!")
                return player_alive


            self.show_world_prompt()
            player_input = input("What do you Choose:").lower()
            if player_input == "e":
                player_alive = self.enter_tile(self.tiles[self.player_position])
                if player_alive and self.tiles[self.player_position].last_tile:
                    world_cleared = True

            if player_input == "c":
                self.player_position = 0
                game_on = False

        return player_alive

