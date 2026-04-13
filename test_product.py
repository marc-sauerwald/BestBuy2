"""Unit tests for the Product class."""
import pytest
from products import Product


class TestProduct:
    """Test suite for the Product class."""

    def test_create_normal_product(self):
        """Test that creating a normal product works."""
        product = Product("MacBook Air M2", price=1450, quantity=100)
        assert product.name == "MacBook Air M2"
        assert product.price == 1450
        assert product.get_quantity() == 100
        assert product.is_active() is True

    def test_create_product_with_empty_name_raises_exception(self):
        """Test that creating a product with empty name raises an exception."""
        with pytest.raises(ValueError):
            Product("", price=1450, quantity=100)

    def test_create_product_with_negative_price_raises_exception(self):
        """Test that creating a product with negative price raises an exception."""
        with pytest.raises(ValueError):
            Product("MacBook Air M2", price=-10, quantity=100)

    def test_product_becomes_inactive_at_zero_quantity(self):
        """Test that when a product reaches 0 quantity, it becomes inactive."""
        product = Product("MacBook Air M2", price=1450, quantity=10)
        assert product.is_active() is True
        product.set_quantity(0)
        assert product.is_active() is False

    def test_product_purchase_modifies_quantity_and_returns_correct_output(self):
        """Test that product purchase modifies the quantity and returns the right output."""
        product = Product("MacBook Air M2", price=1450, quantity=100)
        total_price = product.buy(5)
        assert product.get_quantity() == 95
        assert total_price == 1450 * 5

    def test_buying_more_than_available_raises_exception(self):
        """Test that buying a larger quantity than exists raises an exception."""
        product = Product("MacBook Air M2", price=1450, quantity=10)
        with pytest.raises(ValueError):
            product.buy(15)
