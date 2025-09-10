import GameFile
import game_state

GameFile.initializing()

def Tick():

    for obj in game_state.objects:
        obj.Behaviour()
    return

while True:
    try:
        Tick()

    except ValueError:
        print("Something went wrong")

    else:
        continue