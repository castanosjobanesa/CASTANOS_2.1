class Cart:
    """Manages the items ordered by the customer and calculates totals."""

    def __init__(self, discount_rate, discount_threshold):
        self.items = []
        self.discount_rate = discount_rate
        self.discount_threshold = discount_threshold

    def add_item(self, menu_item, quantity):
        # Update quantity if the item is already in the cart
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