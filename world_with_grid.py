from fight import Fight


class World_Grid:
    """Grid Class for World Navigation"""

    def __init__(self, x_axis, y_axis):
        self.grid = []
        for thing in range(x_axis):
            grid_line = []
            for x in range(y_axis):
                grid_line.append(World_Tile(x_axis, y_axis))
            self.grid.append(grid_line)

    def return_boundary(self, x_coordinate, y_coordinate):

        if x_coordinate < 0 or y_coordinate < 0:
            return False
        else:
            try:
                return self.grid[x_coordinate][y_coordinate].bool
            except IndexError:
                return False

    def return_boundaries(self, x_coordinate, y_coordinate):
        return_list = []

        return_list.append(self.return_boundary(x_coordinate, y_coordinate + 1))
        return_list.append(self.return_boundary(x_coordinate + 1, y_coordinate))
        return_list.append(self.return_boundary(x_coordinate, y_coordinate - 1))
        return_list.append(self.return_boundary(x_coordinate - 1, y_coordinate))
        return return_list

    def get_tile(self, x, y):
        return self.grid[x][y]


class World_Tile:
    """World Tile Class to add into the World Grid"""

    def __init__(self, x_coordinate, y_coordinate, enemy):
        self.position = [x_coordinate, y_coordinate]
        self.bool = True
        self.cleared_flag = False
        self.enemy = enemy



    def show_tile_prompt(self):
        print("You Enter Tile {0}. An Enemy awaits you. Get ready to fight {1} to the death!".format(self.position,
                                                                                                     self.enemy.name))
        print("What do you want to do? [F]ight or Flee to the [C]ity?")



    def show_win_prompt(self):
        #TODO: Add win prompt Method
        """Shown after """




class World:
    """The world Class"""

    def __init__(self, world_grid, entry_coordinates, player, city):
        self.world_grid = world_grid
        self.entry_coordinates = entry_coordinates
        self.player = player
        self.city = city
        self.coordinates = []


    def enter_world(self):
        #TODO: Add Method for first World Entry
        self.enter_tile(self.world_grid.get_tile(self.entry_coordinates))


    def enter_tile(self, tile):
        #TODO: Add Method for Player Entry
        tile.show_tile_prompt()
        player_input = input("Your Choice:").lower()
        if player_input == "f":
            if Fight.fight(self.player, tile.enemy):
                self.show_world_prompt(tile)
            else:
                return False

        if player_input == "c":
            self.enter_city()

    def get_tile_boundaries(self, tile):
        return self.world_grid.return_boundaries(tile.position[0], tile.position[1])

    def show_win_prompt(self, boundaries, tile):
        print("Congratulations! You won! The enemy dropped {0} Gold!".format(tile.enemy.loot))
        print("Where do you want to go next?")

        if boundaries[0]:
            print("[N]orth.")
        if boundaries[1]:
            print("[E]ast.")
        if boundaries[2]:
            print("[S]outh.")
        if boundaries[3]:
            print("[W]est.")
        print("[B]ack to the City")

    def show_world_prompt(self, tile):
        #TODO: Add Method and refactor show_win_prompt in World Tile Class
        """Standard World Prompt, Take Tile as Parameter"""

        print("Congratulations! You won! The enemy dropped {0} Gold!".format(tile.enemy.loot))
        print("Where do you want to go next?")
        self.show_win_prompt()
        self.coordinates = [tile.postion[0], tile.position[1]]
        player_input = input("Your Choice: ").lower()
        if player_input == "n":
            self.enter_tile(self.world_grid.get_tile(self.coordinates[0], self.coordinates[1]+1))
        elif player_input == "e":
            self.enter_tile(self.world_grid.get_tile(self.coordinates[0]+1, self.coordinates[1]))
        elif player_input == "s":
            self.enter_tile(self.world_grid.get_tile(self.coordinates[0], self.coordinates[1]-1))
        elif player_input == "w":
            self.enter_tile(self.world_grid.get_tile(self.coordinates[0]-1, self.coordinates[1]))
        elif player_input == "b":
            self.enter_city()






    def enter_city(self):
        #TODO: Add enter city prompt to use City Class
        self.city.enter_city()
        pass