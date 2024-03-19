  class Bnak:
    name='SBI'
    def account(self,fname,lname,acc_no):
        self.fname=fname
        self.lname=lname
        self.acc_no=acc_no
        self.minbal=5000
        self.total=self.minbal
    def deposit(self,cash):
        self.cash=cash
        self.total+=cash
        print("Your account has been creited by ",self.cash,'and total balance is',self.total)
    def withdraw(self,amount):
        self.amount=amount
        self.total-=amount
        if(self.amount>self.total)
            print("Insufficient amount")
        else:
            print('your account has been credited by',self.amount,'your account balance is',self.total)
