# Bank
#account details (fname,lname,accntno)
#deposit
#withdraw

class Bank():
    bank_name='sbi'
    def account(self,fname,lname,accntno):
        self.fname=fname
        self.lname=lname
        self.accntno=accntno
        self.minbal=5000
        self.totalamount=self.minbal
    def deposit(self,cash):
        self.cash=cash
        self.totalamount+=cash
        print('your',Bank.bank_name,"account has been credited with",self.cash,'and your total account balance is',self.totalamount)
    def withdraw(self,amount):
        self.amount=amount
        self.totalamount-=amount
        if(self.amount>self.totalamount):
            print("you have insufficient balance amount")
        else:
            print('your',Bank.bank_name,"account has been debited by",self.amount,'your balance amount is',self.totalamount)
per1=Bank()
per1.account('Renji','rs',123456789)
per1.deposit(3000)
per1.withdraw(2000)




