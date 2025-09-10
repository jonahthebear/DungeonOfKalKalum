import GameFile
import ObjectClasses
from InventoryClasses import Inventory
import PlayerActions
from ItemClasses import Ability
import game_state

class Creature(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, inventory_size, is_player : bool):
        super().__init__(name, position, hit_points)
        self.names = []
        self.is_player : bool = is_player
        self.Abilities = []
        self.Inventory = Inventory(inventory_size)


    def Player_action(self):

        player_action = input("What would you like to do?").lower()
        word_list = player_action.split()

        #remove useless words
        for conjunction in PlayerActions.conjunctions:
            for word in word_list:
                if word in conjunction:
                    word_list.remove(word)


        for action in game_state.current_room.actions:
            if action in word_list:
                game_state.current_room.actions[action](game_state.current_room)

        PlayerActions.PlayerQuery(word_list, self.Abilities)

        PlayerActions.PlayerQuery(word_list, self.Inventory.items)

        PlayerActions.PlayerQuery(word_list, game_state.current_room.objects_list)

    def Creature_action(self):
        pass # creature logic will go here

    def Behaviour(self):
        if self.is_player:
            self.Player_action()