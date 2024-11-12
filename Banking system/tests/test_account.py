import unittest
from bank.account import Account

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        account = Account("12345")
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw(self):
        account = Account("12345", 100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

if __name__ == '__main__':
    unittest.main()
