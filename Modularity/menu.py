class MenuItem:
    """Represents an individual food item on the menu."""

    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


class Menu:
    """Manages the collection of MenuItems and displays the menu."""

    def __init__(self, menu_data):
        self.items = {}
        for item_id, details in menu_data.items():
            self.items[item_id] = MenuItem(item_id, details["name"], details["price"])

    def display(self, restaurant_name):
        print("\n" + "=" * 45)
        print(f"         WELCOME TO {restaurant_name.upper()}        ")
        print("=" * 45)
        print(f"{'ID':<5} {'Item':<22} {'Price':>15}")
        print("-" * 45)

        for item_id, item in self.items.items():
            print(f"{item_id:<5} {item.name:<22} PHP {item.price:>9.2f}")
        print("=" * 45 + "\n")

    def get_item(self, item_id):
        return self.items.get(item_id)