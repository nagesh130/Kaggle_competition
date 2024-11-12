from .product import Product

class Order:
    def __init__(self, customer): 
        self.customer = customer 
        self.items = [] 
        
    def add_product(self, product, quantity): 
        if product.quantity >= quantity: 
            product.update_quantity(-quantity) 
            self.items.append((product, quantity)) 
        else: 
            raise ValueError("Insufficient quantity in stock")
        
    def total_order_price(self): 
        return sum(product.calculate_total_price(quantity) for product, quantity in self.items)