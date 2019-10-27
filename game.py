# -*- coding: utf-8 -*-
import player
import enemy
import shop
import fight


class Game:
    """The Game Class"""


    def __init__(self, player_name, player_health, shop):
        self.player = player.Player(player_name, player_health)
        self.shop = shop
    
    def print_start(self):
        print("#####Welcome to the Game#####")

    
    def print_menu(self):
        print("Your Turn! Choose what you want to do!\n[1]To fight in the Arena!\n[2]To enter the Shop\n[3]To show your Inventory\n[X]To quit the Game!")
        
    
        
    def run(self):
        game_on = True
        in_shop = True
        self.print_start()
        while game_on:
            self.print_menu()
            player_input = input("Enter your choice!\nYour Choice: ").lower()
            if player_input == "1":
                new_fight = fight.Fight(self.player,enemy.Enemy(20,1,3,1))
                game_on = new_fight.fight()
                
            elif player_input == "2":
                in_shop = True
                while in_shop:
                    in_shop = self.shop.show_shop_prompt(self.player)

            elif player_input == "3":
                self.player.go_to_inventory(self.player)

            elif player_input == "x":
                game_on = False
        print("Game Over!")        

game = Game("Test", 20, shop.Shop())

game.run()