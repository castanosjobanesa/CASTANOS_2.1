import sys


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


class Cart:
    """Manages the items ordered by the customer and calculates totals."""

    def __init__(self, discount_rate=0.10, discount_threshold=500.00):
        self.items = []
        self.discount_rate = discount_rate
        self.discount_threshold = discount_threshold

    def add_item(self, menu_item, quantity):
        # Check if item already exists in cart, update quantity if added again
        for item in self.items:
            if item["menu_item"].item_id == menu_item.item_id:
                item["quantity"] += quantity
                item["total_price"] = item["quantity"] * menu_item.price
                return

        self.items.append({
            "menu_item": menu_item,
            "name": menu_item.name,
            "price": menu_item.price,
            "quantity": quantity,
            "total_price": menu_item.price * quantity
        })

    def calculate_totals(self):
        subtotal = sum(item["total_price"] for item in self.items)
        discount = subtotal * self.discount_rate if subtotal >= self.discount_threshold else 0.0
        grand_total = subtotal - discount
        return subtotal, discount, grand_total


class Restaurant:
    """Main controller class handling the application lifecycle, ordering, and receipt generation."""

    def __init__(self, name, menu_data, discount_rate=0.10, discount_threshold=500.00):
        self.name = name
        self.menu = Menu(menu_data)
        self.discount_rate = discount_rate
        self.discount_threshold = discount_threshold

    def run(self):
        self.menu.display(self.name)

        while True:
            start_order = input("Would you like to place an order? (y/n): ").strip().lower()
            if start_order in ['y', 'yes']:
                break
            elif start_order in ['n', 'no']:
                print(f"\nThank you for visiting {self.name}! Goodbye.")
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        cart = self._get_user_order()
        subtotal, discount, grand_total = cart.calculate_totals()
        self._print_receipt(cart, subtotal, discount, grand_total)

    def _get_user_order(self):
        cart = Cart(self.discount_rate, self.discount_threshold)

        while True:
            try:
                choice = int(input("Enter the Item ID you wish to order: "))
                item = self.menu.get_item(choice)
                if not item:
                    print("Invalid item ID. Please select a valid item from the menu.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a numerical Item ID.")
                continue

            while True:
                try:
                    quantity = int(input(f"Enter quantity for {item.name}: "))
                    if quantity <= 0:
                        print("Quantity must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for quantity.")

            cart.add_item(item, quantity)

            while True:
                again = input("Would you like to order another item? (y/n): ").strip().lower()
                if again in ['y', 'yes', 'n', 'no']:
                    break
                print("Please enter 'y' for yes or 'n' for no.")

            if again in ['n', 'no']:
                break

        return cart

    def _print_receipt(self, cart, subtotal, discount, grand_total):
        print("\n" + "*" * 48)
        print("             OFFICIAL RECEIPT             ")
        print(f"      {self.name.center(36)}      ")
        print("*" * 48)
        print(f"{'Item':<18} {'Qty':<5} {'Price':<11} {'Total':>10}")
        print("-" * 48)

        for item in cart.items:
            print(f"{item['name']:<18} {item['quantity']:<5} PHP {item['price']:<7.2f} PHP {item['total_price']:>7.2f}")

        print("-" * 48)
        print(f"{'Subtotal:':<32} PHP {subtotal:>9.2f}")
        if discount > 0:
            print(f"{'Discount (10% over PHP 500):':<32} -PHP {discount:>8.2f}")
        print(f"{'GRAND TOTAL:':<32} PHP {grand_total:>9.2f}")
        print("*" * 48)
        print("        Thank you for dining with us !    ")
        print("             Have a great day!            \n")