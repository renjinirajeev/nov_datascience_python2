class BasicAccount():
    def __init__(self, name,ac_num:int,balance:float,card_num,card_exp,account_name,opening_balance):
        self.name=name
        self.ac_num=ac_num
        self.balance=balance
        self.card_num=card_num
        self.card_exp=card_exp
        self.account_name=account_name
        self.opening_balance=opening_balance
    def deposit(self,amount:float):
            self.amount=amount
            if(self.amount>0):
                self.balance+=self.amount
                print("Your account has been credited by ",self.amount,"and your current balance is",self.balance)
            else:
                print("Something went error")
    def withdraw(self,amount:float):
            self.amount=amount
            if(self.amount<=self.balance):
                self.balance-=self.amount
                print(self.name, " has withdraw ", self.amount, '.', 'New balance is',self.balance )
                return True
            else:
                print('can not withdraw', self.amount)
                return False
    def get_available_balance(self):
            print(self.balance)
    def get_balance(self):
            print(self.balance)
    def print_balance(self):
            print("your acoount balance is",self.balance)
    def get_name(self):
            print("Account holder:",self.name)
    def get_ac_num(self):
            print("Account number:",self.ac_num)
    # def issue_new_card(self, date):
    #         self.date=date
    def close_account(self):
            self.withdraw(self.balance)
            print(self.balance)
            return True
class PremiumAccount():
    def __init__(self,overdraft,account_name,opening_balance):
        self.overdraft=overdraft
        self.overdraft_limit=5000
        self.account_name=account_name
        self.opening_balance=opening_balance

    def set_ovedraft_limit(self):
        self.new_limit = 5000

    def deposit(self, amount: float):
        self.amount = amount
        if (self.amount > 0):
            self.balance += self.amount
            print("Your account has been credited by ", self.amount, "and your current balance is", self.balance)
        else:
            print("Something went error")

    def withdraw(self, amount: float):
        self.amount = amount
        if (self.amount <= (self.balance+self.overdraft_limit)):
            self.balance -= self.amount
            print(self.name, " has withdraw ", self.amount, '.', 'New balance is', self.balance)
            return True
        else:
            print('can not withdraw', self.amount)
            return False

    def get_available_balance(self):
            print(self.balance+self.overdraft_limit)
    def get_balance(self):
             if(self.overdraft_limit-self.balance<=5000):
                 print("account blance is:",self.overdraft-self.balance)
             else:
                 print(self.balance)

    def close_account(self):
        self.withdraw(self.balance)
        if(self.overdraft<0):
            print("can not close account due to customer being overdrawn by", self.overdraft_limit)
per1=BasicAccount('Renji',23466321,2356.1,346256247,'12/27','Basic Account',500)
per1.get_balance()



        






























