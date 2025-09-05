import ObjectClasses
from InventoryClasses import Inventory
import PlayerActions
from ItemClasses import Ability
import game_state

class Creature(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, inventory_size, is_player : bool):
        super().__init__(name, position, hit_points)

        self.is_player : bool = is_player
        self.Abilities = []
        self.Abilities.append(Inventory(inventory_size))

    def player_action(self):

        player_action = input("What would you like to do?").lower()
        word_list = player_action.split()

        #remove useless words

        target = ""

        #room player actions
        PlayerActions.player_query(word_list, game_state.rooms, target)

        #player ability actions
        PlayerActions.player_query(word_list, self.Abilities, target)

        #player item actions

        #player meta actions

    def creature_action(self):
        pass # creature logic will go here

    def behaviour(self):
        if self.is_player:
            self.player_action()