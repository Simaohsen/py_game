

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


class World_Tile:
    """World Tile Class to add into the World Grid"""

    def __init__(self, x_coordinate, y_coordinate, enemy, intro_string, world_grid):
        self.position = (x_coordinate, y_coordinate)
        self.bool = True
        self.visited_flag = False
        self.enemy = enemy
        self.intro_string = intro_string
        self.boundaries = world_grid.return_boundaries()

    def enter_tile(self):
        #TODO: Add Method for Player Entry
        pass
