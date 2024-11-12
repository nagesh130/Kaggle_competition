import unittest
from ecommerce.product import Product

class TestProduct(unittest.TestCase):
    def test_update_quantity(self):
        product = Product("Laptop", 1000, 50)
        product.update_quantity(10)
        self.assertEqual(product.quantity, 60)

    def test_calculate_total_price(self):
        product = Product("Laptop", 1000, 50)
        total = product.calculate_total_price(2)
        self.assertEqual(total, 2000)

if __name__ == '__main__':
    unittest.main()