from ItemClasses import Ability

class Inventory(Ability):
    def __init__(self, maximum_items):
        name = "Inventory"
        self.maximum_items = maximum_items
        self.items = []
        self.names = {'inventory', 'bag', 'backpack'}

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def use(self, item_name):
        if not self.items.__contains__(item_name):
            return print(f"Inventory has no {item_name}")

        for item in self.items:
            if item.name == item_name:
                item.Action()
                break

        return

    def check_inventory(self):
        print("You open your bag")

        if len(self.items) == 0:
            print("Your bag is empty...")
            return
        print("your bag contains:")
        for item in self.items:
            print(item.name)

        return

    actions = {
        "open": check_inventory,
        "check": check_inventory,
        "view": check_inventory,
    }