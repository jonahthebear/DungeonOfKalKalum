conjunctions = ['the', 'in', 'on', 'with', 'for', 'a']


def filter_list(input, list) -> bool:

    for item in list:
        if item in input:
            return True

    return False



def PlayerQuery(player_input, items_list):

    for item in items_list:
        if filter_list(player_input, item.names):
                for action in item.actions:
                    if action in player_input:
                        item.actions[action](item)

    return