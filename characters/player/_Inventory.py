# characters/player/_Inventory.py
class Inventory:
    def __init__(self):
        self._inventory = []

    def add(self, item):
        self._inventory.append(item)

    def remove(self, item):
        if item in self._inventory:
            self._inventory.remove(item)
        else:
            print(f"{item} is not in the inventory.")

    def show(self):
        if self._inventory:
            print("Inventory:")
            for item in self._inventory:
                print(f"- {item}")
        else:
            print("The inventory is empty.")

    def count(self):
        return len(self._inventory)

    def has_item(self, item):
        return item in self._inventory

    def clear(self):
        self._inventory.clear()
