import time
from display import clear_screen


class Fight:

    """The fight Class"""

    def __init__(self, player, enemy):

        self.player = player
        self.enemy = enemy

    def fight(self):

        turn_counter = 1
        last_turn_fight_output_line = ""
        while self.player.health > 0 and self.enemy.health > 0:

            clear_screen()
            print(self.render_fight_overview(self.player, self.enemy))
            if not last_turn_fight_output_line == "":
                print(last_turn_fight_output_line[0])
                print(last_turn_fight_output_line[1])
                print(last_turn_fight_output_line[2])

            player_turn_dmg = self.player.inventory.weapon.dmg_roll()
            self.enemy.health -= player_turn_dmg

            player_turn_output_line = self.create_roll_string(self.player.name, player_turn_dmg, self.enemy.name,
                                                                       self.enemy.health)


            time.sleep(2)
            enemy_turn_dmg = self.enemy.dmg_roll() - self.player.inventory.armor.armor_value - self.player.inventory.shield.block_roll()

            if enemy_turn_dmg < 0:
                enemy_turn_dmg = 0

            self.player.health -= enemy_turn_dmg

            enemy_turn_output_line = self.create_roll_string(self.enemy.name, enemy_turn_dmg, self.player.name,
                                                                           self.player.health)
            fight_output_line = "______________________Turn {0}______________________".format(turn_counter),player_turn_output_line, enemy_turn_output_line

            clear_screen()
            print(self.render_fight_overview(self.player, self.enemy))
            if not last_turn_fight_output_line == "":
                print(last_turn_fight_output_line[0])
                print(last_turn_fight_output_line[1])
                print(last_turn_fight_output_line[2])

            print(fight_output_line[0])
            print(fight_output_line[1])
            print(fight_output_line[2])

            if self.enemy.health <= 0 and self.player.health > 0:
                self.player.add_gold(self.enemy.loot)
                print("You Win!")
                return True

            if self.player.health <= 0:
                print("You lose!")
                return False
            turn_counter += 1
            last_turn_fight_output_line = fight_output_line
            time.sleep(4)


    def create_roll_string(self, attacker_name, turn_dmg, victim_name, victim_health):
        return "{0} deals {1} DMG! {2} has {3} Health left!".format(attacker_name, turn_dmg, victim_name, victim_health)


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


