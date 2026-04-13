# Best Buy 2.0

An electronic store management system built with Python, featuring product management, promotions, and order processing.

## Features

- **Product Management**: Regular products, non-stocked products (e.g., software licenses), and limited products (e.g., shipping fees)
- **Promotions System**: Percentage discounts, second item at half price, buy 2 get 1 free
- **Order Processing**: Interactive menu for browsing and purchasing products
- **Unit Testing**: Comprehensive test suite using pytest

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/marc-sauerwald/BestBuy2.git
   cd BestBuy2
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Usage

Run the store application:
```bash
python main.py
```

Run unit tests:
```bash
python -m pytest test_product.py -v
```

Run linting:
```bash
python -m pylint *.py
```

## Project Structure

- `main.py` - Main application with user interface
- `products.py` - Product classes (Product, NonStockedProduct, LimitedProduct)
- `promotions.py` - Promotion classes (PercentDiscount, SecondHalfPrice, ThirdOneFree)
- `store.py` - Store class for managing products and orders
- `test_product.py` - Unit tests for Product class
- `requirements.txt` - Project dependencies
- `README.md` - Project documentation

## License

This project is open source and available under the MIT License.

## Author

Marc Sauerwald

Built as part of the Masterschool Software Engineering Program
