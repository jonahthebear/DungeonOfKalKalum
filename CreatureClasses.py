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

    def Player_action(self):

        player_action = input("What would you like to do?").lower()
        word_list = player_action.split()

        #remove useless words
        for conjunction in PlayerActions.conjunctions:
            for word in word_list:
                if word in conjunction:
                    word_list.remove(word)

        PlayerActions.PlayerQuery(word_list, game_state.rooms)

        PlayerActions.PlayerQuery(word_list, self.Abilities)

    def Creature_action(self):
        pass # creature logic will go here

    def Behaviour(self):
        if self.is_player:
            self.Player_action()