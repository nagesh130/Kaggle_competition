from bank.account import Account
from bank.customer import Customer
from bank.transaction import Transaction

# Create instances
account1 = Account("12345", 1000)
customer = Customer("Alice", "001")

# Customer adds account
customer.add_account(account1)

# Create transactions
transaction1 = Transaction(account1, 200, "deposit")
transaction2 = Transaction(account1, 150, "withdraw")

# Process transactions
transaction1.process()
transaction2.process()

# Get account balance
print("Account balance:", account1.get_balance())