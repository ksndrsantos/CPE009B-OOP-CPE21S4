"""
  main.py
"""

import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456, account_firstname="Royce", account_lastname="Chua",current_balance=1000, address="Silver Street Quezon City", email="roycechua123@gmail.com")

print("Account 1")
Account1.account_firstname = "Royce"
Account1.account_lastname = "Chua"
Account1.current_balance = 1000
Account1.address = "Silver Street Quezon City"
Account1.email = "roycechua123@gmail.com"

print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = Accounts.Accounts(account_number=654321,account_firstname="John", account_lastname="Doe", current_balance=2000, address="Gold Street Quezon City", email="johndoe@yahoo.com")
Account2.account_firstname = "John"
Account2.account_lastname = "Doe"
Account2.current_balance = 2000
Account2.address = "Gold Street Quezon City"
Account2.email = "johndoe@yahoo.com"

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

ATM1 = ATM.ATM()
ATM1.deposit(Account1,500)
ATM1.check_currentbalance(Account1)

ATM1.deposit(Account2,300)
ATM1.check_currentbalance(Account2)

print("Transaction Summary for Account 1:")
Account1.view_transactionsummary()

print("Transaction Summary for Account 2:")
Account2.view_transactionsummary()


