"""Store class for managing products."""
import products


class Store:
    """Represents a store that holds and manages products."""

    def __init__(self, product_list: list = None):
        """
        Initialize a new Store.

        Args:
            product_list: Optional list of Product instances to start with
        """
        if product_list is None:
            self.products = []
        else:
            self.products = list(product_list)

    def add_product(self, product):
        """
        Add a product to the store.

        Args:
            product: Product instance to add
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.

        Args:
            product: Product instance to remove
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Return the total quantity of all items in the store.

        Returns:
            Sum of quantities across all products
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list:
        """
        Return all active products in the store.

        Returns:
            List of active Product instances
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Process an order for multiple products.

        Args:
            shopping_list: List of tuples (Product, quantity)

        Returns:
            Total price of the order
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    """Test the Store class."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(all_products[0], 1), (all_products[1], 2)]))


if __name__ == "__main__":
    main()
