import ObjectClasses
from InventoryClasses import Inventory
class Item(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position,  hit_points, ability_type : str):
        super().__init__(name, position, hit_points)

        self.ability_type = ability_type

    def Action(self):
        pass

    def PickUp(self, inventory : Inventory):
        inventory.add(self)


class PotionBottle(Item):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, uses):

        Item.__init__(self, name, position, hit_points, uses)

        self.uses = uses

healthpotion = PotionBottle("Healthpotion", ObjectClasses.Position(100, 100, 100), 5, 3)