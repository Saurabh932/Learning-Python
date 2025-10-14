'''
    Q2.
'''

class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
        
    def detils(self, debit, credit):
        if debit and credit == 0:
            print(f"{debit} is debited from your account.")
            new_bal = self.balance - debit
            print(f"Your new balance is {new_bal}.")
            
        elif credit and debit == 0:
            print(f"{credit} is credited your account.")
            new_bal = self.balance + credit
            print(f"Your new balance is {new_bal}")
            
        else:
            print(f"No changes to your account.")
            
acc = Account(365646464, 5000)
acc.detils(100, 0)