# -*- coding: utf-8 -*-
import player
import enemy
import shop
import fight
from world import World, World_Tile
from city import City


class Game:
    """The Game Class"""


    def __init__(self):
        self.player = player.Player("Player 1", 20)
        self.city = City(self.player, World(self.player, [World_Tile(enemy.Simple_Enemy(), False), World_Tile(enemy.Medium_Enemy(), False), World_Tile(enemy.Hard_Enemy(), False), World_Tile(enemy.Endboss(), True)]))
    
    def print_start(self):
        print("#####Welcome to the Game#####")

    
    def print_menu(self):
        print("Your Turn! Choose what you want to do!\n[1]To fight in the Arena!\n[2]To enter the Shop\n[3]To show your Inventory\n[X]To quit the Game!")
        
    
        
    def run(self):
        self.print_start()
        game_on = True
        while game_on:
            game_on = self.city.enter_city()

game = Game()

game.run()