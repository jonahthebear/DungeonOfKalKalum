import ObjectClasses
from InventoryClasses import Inventory
import PlayerActions

class Creature(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, inventory_size, isPlayer : bool):
        super().__init__(name, position, hit_points)

        self.isPlayer : bool = isPlayer
        self.Inventory = Inventory(inventory_size)

    def Player_action(self):
        player_action = input("What would you like to do?").lower()
        wordList = player_action.split()

        #inventory
        if PlayerActions.PlayerQuery(wordList, PlayerActions.InventoryVerbs, PlayerActions.InventoryNames):
            PlayerActions.CheckInventory(self.Inventory)

        #uses


        #attack

    def Creature_action(self):
        pass # creature logic will go here

    def Behaviour(self):
        if self.isPlayer:
            self.Player_action()