def PlayerQuery(player_input, verb_list, noun_list):

    query = False

    for verb in verb_list:
        if verb in player_input:
            query = True
            break

    if query:
        for noun in noun_list:
            if noun in player_input:
                query = True

    return query

InventoryNames = {'inventory', 'bag', 'backpack'}
InventoryVerbs = ('open', 'check')

def CheckInventory(inventory):
    return inventory.GetItemNames()