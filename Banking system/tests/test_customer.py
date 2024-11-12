import unittest
from bank.customer import Customer
from bank.account import Account

class TestCustomer(unittest.TestCase):
    def test_add_account(self):
        customer = Customer("Alice", "001")
        account = Account("12345")
        customer.add_account(account)
        self.assertIn(account, customer.accounts)

if __name__ == '__main__':
    unittest.main()
