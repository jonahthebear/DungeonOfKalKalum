class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Object:
    def __init__(self, name, position: Position):
        self.name = name
        self.position = position
        #objects should have descriptions but those should be read from a file, not coded into the actual program


class Damageable:
    def __init__(self, hit_points):
        self.hit_points = hit_points

    def Damage(self, damage):
        self.hit_points -= damage

class DamageableObject(Object, Damageable):
    def __init__(self, name, position: Position, hit_points):
        Object.__init__(self, name, position)
        Damageable.__init__(self, hit_points)


class Creature(DamageableObject):
    def __init__(self, name, position: Position, hit_points):
        super().__init__(name, position, hit_points)

    #A behaviour class reference can go here so that creatures can be created with certain behaviours or something

class Room:
    pass

class Door(Object):
    def __init__(self, name, position: Position, connecting_room : Room):
        Object.__init__(self, name, position)

        self.connecting_room = connecting_room