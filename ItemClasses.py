import ObjectClasses
from InventoryClasses import Inventory

class Item(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position, size, hit_points):
        super().__init__(name, position, hit_points)

    def Action(self):
        pass

    def PickUp(self, inventory : Inventory):
        inventory.add(self)


class PotionBottle(Item):
    def __init__(self, name, position: ObjectClasses.Position, size, hit_points, uses):

        Item.__init__(self, name, position, size, hit_points)

        self.uses = uses
