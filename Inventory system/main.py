from ecommerce.product import Product
from ecommerce.customer import Customer
from ecommerce.order import Order

# Create instances
product1 = Product("Laptop", 1000, 50)
product2 = Product("Mouse", 50, 100)
customer = Customer("Alice", "alice@example.com")

# Customer places an order
order = Order(customer)
customer.place_order(order)

# Add products to the order
order.add_product(product1, 2)
order.add_product(product2, 4)

# Calculate total order price
print("Total order price:", order.total_order_price())