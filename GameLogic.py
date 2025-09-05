import GameFile
import game_state

GameFile.initializing()

def tick():

    for obj in game_state.objects:
        obj.behaviour()
    return

while True:
    try:
        tick()

    except ValueError:
        print("Something went wrong")
    else:
        continue