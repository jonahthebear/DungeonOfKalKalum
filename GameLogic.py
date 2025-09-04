import ItemClasses
import ObjectClasses
import CreatureClasses

Objects : list[ObjectClasses.Object] = []

def Initializing():

    player = CreatureClasses.Creature("player", ObjectClasses.Position(0,0,0), 100, 10, True)
    testItem = ItemClasses.Item("testItem", ObjectClasses.Position(0, 0, 0), 100, "item")
    Objects.append(player)
    player.Abilities[0].add(testItem)

Initializing()

def Tick():

    for obj in Objects:
        obj.Behaviour()
    return

while True:
    try:
        Tick()

    except ValueError:
        print("Something went wrong")
    else:
        break