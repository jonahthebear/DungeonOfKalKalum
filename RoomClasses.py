import CreatureClasses
import ObjectClasses

class Room:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.objects_list = []
        self.names = ['room', 'chamber', 'around']
        self.description = ""

    def examine_room(self):
        print("you examine the room")
        print(self.description)
        print("in the room you see")
        for obj in self.objects_list:
            if type(obj) == CreatureClasses.Creature and obj.is_player:
                continue
            print(obj.name)

    actions = {
        "examine" : examine_room,
        "look" : examine_room,
        "check" : examine_room,
    }


class Door(ObjectClasses.Object):
    def __init__(self, name, position: ObjectClasses.Position):
        super().__init__(name, position)
