import sys
from config import MENU, RESTAURANT_NAME, DISCOUNT_RATE, DISCOUNT_THRESHOLD
from menu import Menu
from order import Cart


class RestaurantApp:
    """Main application controller."""

    def __init__(self):
        self.name = RESTAURANT_NAME
        self.menu = Menu(MENU)
        self.discount_rate = DISCOUNT_RATE
        self.discount_threshold = DISCOUNT_THRESHOLD

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


def main():
    app = RestaurantApp()
    app.run()


if __name__ == "__main__":
    main()