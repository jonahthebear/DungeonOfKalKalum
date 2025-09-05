import inspect

def player_query(player_input, items_list, target):

    if "my" in player_input:


    for item in items_list:

        for name in item.names:
            if name in player_input:
                for action in item.actions:
                    if action in player_input:
                        if len(inspect.signature(item.actions[action]).parameters) == 1:
                            item.actions[action](item)
                        else:
                            item.actions[action](item, target)

    return