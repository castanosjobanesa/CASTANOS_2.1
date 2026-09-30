from restaurant import Restaurant

MENU_DATA = {
    1: {"name": "Sizzling Sisig", "price": 185.00},
    2: {"name": "Pork Sinigang", "price": 220.00},
    3: {"name": "Garlic Rice", "price": 35.00},
    4: {"name": "Chicken Inasal", "price": 165.00},
    5: {"name": "Halo-Halo Special", "price": 95.00}
}


def main():
    # Initialize the Restaurant instance with name and menu data
    restaurant_app = Restaurant(
        name="J&L RESTAURANT",
        menu_data=MENU_DATA,
        discount_rate=0.10,
        discount_threshold=500.00
    )

    # Start the application loop
    restaurant_app.run()


if __name__ == "__main__":
    main()