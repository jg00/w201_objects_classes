
class BankAccount:
    def __init__(self, first_name, last_name, middle_name, account_type, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_type = account_type
        self.balance = balance

        if (self.balance >= 100):
            self.status = "Opened"


    def transfer(self, amount_to_transfer, transfer_to_account):
        self.balance = self.balance - amount_to_transfer
        if self.balance < 0:
            self.balance = self.balance - 35

        transfer_to_account.balance = transfer_to_account.balance + amount_to_transfer


    def withdraw(self, amount_to_withdraw):
        self.balance = self.balance - amount_to_withdraw
        if self.balance < 0:
            self.balance = self.balance - 35


jill_acct = BankAccount("Jill","Dobbs","Mills","Checking",100)
brent_acct = BankAccount("Jane","Grear","Wells","Checking",100)

# Transfer
jill_acct.transfer(50,brent_acct)
print(jill_acct.balance)
print(brent_acct.balance)

# Withdraw
jill_acct.transfer(10,brent_acct)
print(jill_acct.balance)

