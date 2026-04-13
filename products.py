"""Product class for the Best Buy store."""


class Product:
    """Represents a product available in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new Product.

        Args:
            name: Product name (must not be empty)
            price: Product price (must be non-negative)
            quantity: Initial quantity in stock (must be non-negative)

        Raises:
            ValueError: If name is empty, or price/quantity is negative
        """
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity in stock."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the quantity. Deactivates product if quantity reaches 0.

        Args:
            quantity: New quantity value
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Return True if product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a string representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """
        Buy a given quantity of the product.

        Args:
            quantity: Number of items to purchase

        Returns:
            Total price of the purchase

        Raises:
            ValueError: If quantity is invalid or exceeds available stock
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock. Available: {self.quantity}")
        if not self.active:
            raise ValueError("Product is not active")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


def main():
    """Test the Product class."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
