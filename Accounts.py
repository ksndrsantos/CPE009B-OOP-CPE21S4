"""
  Accounts.py
"""

class Accounts():
    def __init__(self,account_number,account_firstname,account_lastname,current_balance, address,email): 
       self.account_number =account_number
       self.account_firstname = account_firstname
       self.account_lastname = account_lastname
       self. current_balance = current_balance
       self. address = address
       self. email = email
       self.transaction_history =[]

    def update_address(self, new_address):
      self.address = new_address
  
    def update_email(self, new_email):
      self.email = new_email

    def additional_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.current_balance
        }
        self.transaction_history.append(transaction)  

    

    def view_transactionsummary(self):
        print(f"Transaction summary for {self.account_firstname} {self.account_lastname}:")
        for transaction in self.transaction_history:
            print(f"{transaction['type']}: PHP{transaction['amount']}, Balance: PHP{transaction['balance']}")