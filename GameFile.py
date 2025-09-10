import CreatureClasses
import RoomClasses
import ItemClasses
import ObjectClasses
import game_state

def initializing():

    player = CreatureClasses.Creature("player", ObjectClasses.Position(0,0,0), 100, 10, True)
    test_item = ItemClasses.Item("test item", ObjectClasses.Position(0, 0, 0), 100, "item")
    test_potion = ItemClasses.PotionBottle("test potion", ObjectClasses.Position(0,0,0), 100, "potion")

    game_state.objects.append(player)

    player.Inventory.add(test_item)
    player.Inventory.add(test_potion)

    test_room = RoomClasses.Room("test room", ObjectClasses.Position(0,0,0))
    test_room.objects_list.append(player)

    game_state.rooms.append(test_room)

    test_furniture = ItemClasses.Item("test furniture", ObjectClasses.Position(0,0,0), 100, "item")
    test_furniture2 = ItemClasses.Item("test furniture 2", ObjectClasses.Position(0,0,0), 100, "item")
    test_room.objects_list.append(test_furniture)

    test_room2 = RoomClasses.Room("test room 2", ObjectClasses.Position(0,0,0))
    test_room2.objects_list.append(test_furniture2)

    game_state.current_room = test_room

    test_door = RoomClasses.Door("test door", ObjectClasses.Position(0, 0, 0), 2)
    test_room.objects_list.append(test_door)


    game_state.rooms.append(test_room)
    game_state.rooms.append(test_room2)

    return