class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        
