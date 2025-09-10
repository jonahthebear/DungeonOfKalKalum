class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Object:
    def __init__(self, name, position: Position, ):
        self.name = name
        self.position = position

    def behaviour(self):
        pass

class Damageable:
    def __init__(self, hit_points):
        self.hit_points = hit_points

    def Damage(self, damage):
        self.hit_points -= damage

class DamageableObject(Object, Damageable):
    def __init__(self, name, position: Position, hit_points):
        Object.__init__(self, name, position)
        Damageable.__init__(self, hit_points)
