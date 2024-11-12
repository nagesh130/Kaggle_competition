import unittest
from bank.account import Account
from bank.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def test_process_deposit(self):
        account = Account("12345", 100)
        transaction = Transaction(account, 50, "deposit")
        transaction.process()
        self.assertEqual(account.get_balance(), 150)

    def test_process_withdraw(self):
        account = Account("12345", 100)
        transaction = Transaction(account, 50, "withdraw")
        transaction.process()
        self.assertEqual(account.get_balance(), 50)

if __name__ == '__main__':
    unittest.main()
