"""
  ATM.py
"""

class ATM:
    serial_number = 0

    def deposit(self, account, amount):
        account.current_balance += amount
        account.additional_transaction("Deposit", amount)  
        print(f"Deposit of PHP{amount} to {account.account_firstname} {account.account_lastname}'s account is complete.")

    def withdraw(self, account, amount):
        account.current_balance -= amount
        account.additional_transaction("Withdrawal", amount)  
        print(f"Withdrawal of PHP{amount} from {account.account_firstname} {account.account_lastname}'s account is complete.")

    def check_currentbalance(self, account):
        print(f"Current balance for {account.account_firstname} {account.account_lastname}: PHP{account.current_balance}")
