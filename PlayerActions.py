conjunctions = ['the', 'in', 'on', 'with', 'for']

def PlayerQuery(player_input, items_list):

    for item in items_list:

        for name in item.names:
            if name in player_input:
                for action in item.actions:
                    if action in player_input:
                        item.actions[action](item)

    return