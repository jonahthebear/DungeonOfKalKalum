class Inventory:
    def __init__(self, maximum_items):
        self.maximum_items = maximum_items
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def Use(self, item_name):
        if not self.items.__contains__(item_name):
            return print(f"Inventory has no {item_name}")

        for item in self.items:
            if item.name == item_name:
                item.Action()
                break

        return