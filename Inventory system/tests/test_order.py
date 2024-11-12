import unittest
from ecommerce.product import Product
from ecommerce.customer import Customer
from ecommerce.order import Order

class TestOrder(unittest.TestCase):
    def test_add_product(self):
        customer = Customer("Alice", "alice@example.com")
        order = Order(customer)
        product = Product("Laptop", 1000, 50)
        order.add_product(product, 2)
        self.assertEqual(product.quantity, 48)
        self.assertIn((product, 2), order.items)

    def test_total_order_price(self):
        customer = Customer("Alice", "alice@example.com")
        order = Order(customer)
        product1 = Product("Laptop", 1000, 50)
        product2 = Product("Mouse", 50, 100)
        order.add_product(product1, 2)
        order.add_product(product2, 4)
        total = order.total_order_price()
        self.assertEqual(total, 2200)

if __name__ == '__main__':
    unittest.main()
