import ObjectClasses

class Ability:
    def __init__(self, name):
        self.name = name
        self.actions = {}

class Item(ObjectClasses.DamageableObject):
    def __init__(self, name, position: ObjectClasses.Position,  hit_points, ability_type : str):
        super().__init__(name, position, hit_points)

        self.ability_type = ability_type
        self.names = []
        actions = {}

    def PickUp(self, inventory):
        inventory.add(self)



class PotionBottle(Item):
    def __init__(self, name, position: ObjectClasses.Position, hit_points, uses):

        Item.__init__(self, name, position, hit_points, uses)

        self.uses = uses

    def drink(self, target):
        return

    actions = {
        "drink": drink
    }