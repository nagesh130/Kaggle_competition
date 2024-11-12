class Customer:
    def __init__(self, name, cutomer_id):
        self.name = name
        self.customer_id = cutomer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)