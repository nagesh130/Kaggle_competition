import unittest
from ecommerce.customer import Customer
from ecommerce.order import Order
from ecommerce.product import Product

class TestCustomer(unittest.TestCase):
    def test_place_order(self):
        customer = Customer("Alice", "alice@example.com")
        order = Order(customer)
        customer.place_order(order)
        self.assertIn(order, customer.orders)

if __name__ == '__main__':
    unittest.main()
