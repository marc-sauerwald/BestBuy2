"""Promotion classes for the Best Buy store."""
from abc import ABC, abstractmethod


class Promotion(ABC):  # pylint: disable=too-few-public-methods
    """Abstract base class for all promotions."""

    def __init__(self, name: str):
        """
        Initialize a promotion.

        Args:
            name: Name/description of the promotion
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, price: float, quantity: int) -> float:
        """
        Calculate the discounted price after applying the promotion.

        Args:
            price: Original price per item
            quantity: Number of items being purchased

        Returns:
            Total price after promotion is applied
        """


class PercentDiscount(Promotion):  # pylint: disable=too-few-public-methods
    """Percentage discount promotion (e.g., 30% off)."""

    def __init__(self, name: str, percent: float):
        """
        Initialize a percentage discount promotion.

        Args:
            name: Name of the promotion
            percent: Discount percentage (e.g., 30 for 30% off)
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price: float, quantity: int) -> float:
        """Apply percentage discount to the total price."""
        total = price * quantity
        discount = total * (self.percent / 100)
        return total - discount


class SecondHalfPrice(Promotion):  # pylint: disable=too-few-public-methods
    """Second item at half price promotion."""

    def apply_promotion(self, price: float, quantity: int) -> float:
        """
        Apply second item at half price.

        For every pair of items, the second one is half price.
        """
        pairs = quantity // 2
        remaining = quantity % 2

        pair_cost = pairs * (price + price * 0.5)
        remaining_cost = remaining * price

        return pair_cost + remaining_cost


class ThirdOneFree(Promotion):  # pylint: disable=too-few-public-methods
    """Buy 2, get 1 free promotion."""

    def apply_promotion(self, price: float, quantity: int) -> float:
        """
        Apply buy 2 get 1 free promotion.

        For every 3 items, only 2 are charged.
        """
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * price
