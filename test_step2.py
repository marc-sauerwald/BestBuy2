"""Test script for Step 2 - New product types."""
import products
import store


def main():
    """Test the new product types."""
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    best_buy = store.Store(product_list)

    print("=== All Products ===")
    for product in best_buy.get_all_products():
        print(product.show())

    print(f"\nTotal quantity in store: {best_buy.get_total_quantity()}")

    # Test NonStockedProduct
    print("\n=== Test NonStockedProduct ===")
    windows = product_list[3]
    print(f"Buy 5 Windows Licenses: ${windows.buy(5)}")
    print(f"After purchase: {windows.show()}")

    # Test LimitedProduct
    print("\n=== Test LimitedProduct ===")
    shipping = product_list[4]
    print(f"Buy 1 Shipping: ${shipping.buy(1)}")

    # Test LimitedProduct exception
    print("\n=== Test LimitedProduct Exception ===")
    try:
        shipping.buy(2)
    except ValueError as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()
