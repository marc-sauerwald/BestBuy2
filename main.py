"""Main module for the Best Buy store application."""
import products
import store


def list_all_products(best_buy):
    """Display all active products in the store."""
    print("\n------")
    all_products = best_buy.get_all_products()
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}")
    print("------")


def show_total_amount(best_buy):
    """Display the total quantity of items in the store."""
    total = best_buy.get_total_quantity()
    print(f"\nTotal of {total} items in store")


def make_order(best_buy):
    """Handle the order process with user input."""
    print("------")
    all_products = best_buy.get_all_products()

    # Display products
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}")
    print("------")

    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_input = input("Which product # do you want? ")

        # Empty input means finish ordering
        if product_input == "":
            break

        try:
            product_num = int(product_input)
            if product_num < 1 or product_num > len(all_products):
                print("Error adding product!")
                continue

            quantity_input = input("What amount do you want? ")
            quantity = int(quantity_input)

            if quantity <= 0:
                print("Error adding product!")
                continue

            selected_product = all_products[product_num - 1]
            shopping_list.append((selected_product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Error adding product!")

    # Process the order if there are items
    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print("\n********")
            print(f"Order made! Total payment: ${total_price}")
        except ValueError as e:
            print(f"\nError while making order! {e}")


def start(best_buy):
    """
    Main menu loop for the store interface.

    Args:
        best_buy: Store instance to operate on
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_all_products(best_buy)

        elif choice == "2":
            show_total_amount(best_buy)

        elif choice == "3":
            make_order(best_buy)

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    """Initialize inventory and start the store interface."""
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)


if __name__ == "__main__":
    main()
