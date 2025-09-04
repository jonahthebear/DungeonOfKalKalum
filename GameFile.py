import CreatureClasses
import RoomClasses
import ItemClasses
import ObjectClasses
import game_state

def initializing():

    player = CreatureClasses.Creature("player", ObjectClasses.Position(0,0,0), 100, 10, True)
    test_item = ItemClasses.Item("test item", ObjectClasses.Position(0, 0, 0), 100, "item")
    game_state.objects.append(player)
    player.Abilities[0].add(test_item)

    test_room = RoomClasses.Room("test room", ObjectClasses.Position(0,0,0))
    test_room.objects_list.append(player)

    game_state.rooms.append(test_room)

    test_furniture = ItemClasses.Item("test furniture", ObjectClasses.Position(0,0,0), 100, "item")
    test_room.objects_list.append(test_furniture)

    return