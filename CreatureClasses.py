import ObjectClasses
from ItemClasses import Ability
from InventoryClasses import Inventory

import PlayerActions

class Creature(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, inventory_size, is_player : bool):
        super().__init__(name, position, hit_points)

        self.isPlayer : bool = is_player
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

        PlayerActions.PlayerQuery(word_list, self.Abilities)

    def Creature_action(self):
        pass # creature logic will go here

    def Behaviour(self):
        if self.isPlayer:
            self.Player_action()