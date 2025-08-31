import ObjectClasses

class Room:
    pass

class Door(ObjectClasses.Object):
    def __init__(self, name, position: ObjectClasses.Position):
        self.name = name
        self.position = position