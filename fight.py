import time
import os


class Fight:

    """The fight Class"""

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

    def fight(self):

        while self.player.health > 0 and self.enemy.health > 0:

            self.clear_screen()
            print(self.render_fight_overview(self.player, self.enemy))
            time.sleep(2)
            player_turn_dmg = self.player.inventory.weapon.dmg_roll()
            self.enemy.health -= player_turn_dmg



            print(self.create_roll_string(self.player.name, player_turn_dmg, self.enemy.name,
                                                                       self.enemy.health))
            if self.enemy.health <= 0:
                print("You Win!")
                return True

            time.sleep(2)
            enemy_turn_dmg = self.enemy.dmg_roll() - self.player.inventory.armor.armor_value - self.player.inventory.shield.block_roll()

            if enemy_turn_dmg < 0:
                enemy_turn_dmg = 0

            self.player.health -= enemy_turn_dmg
            print(self.create_roll_string(self.enemy.name, enemy_turn_dmg, self.player.name,
                                                                           self.player.health))

            if self.player.health <= 0:
                print("You lose!")
                return False



    def create_roll_string(self, attacker_name, turn_dmg, victim_name, victim_health):
        return "{0} deals {1} DMG! {2} has {3} Health left!".format(attacker_name, turn_dmg, victim_name, victim_health)

    def show_fight_art(self):
        print("""
                 /| __________________
             O|===|* >________________>
                 \|""")


    def render_healthbar(self, character):

        health_string = "#"*character.health + "."*(20 -character.health)
        return health_string

    def render_fight_overview(self, player, enemy):
        line1 = self.render_healthbar(player) + "           " + self.render_healthbar(enemy)
        line2 = "Player                         Enemy"
        line3 = str(player.health) + " HP                          " + str(enemy.health) +" HP"

        return line1 + "\n" +line2 + "\n" + line3


    def render_fight(self):
        pass


    def clear_screen(self):
        os.system('cls')