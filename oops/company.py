# class company
# id,fname,lname,age,prof,company_name
# 5 employee with same company and prof

class Company():
    company_name='ABCB'
    prof='developer'
    def setvalue(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,Company.company_name,Company.prof)
emp1=Company()
emp1.setvalue(101,'ram','r',22)
emp1.printvalue()
emp2=Company()
emp2.setvalue(102,'ravi','s',45)
emp2.printvalue()
emp3=Company()
emp3.setvalue(103,'sai','m',34)
emp3.printvalue()
emp4=Company()
emp4.setvalue(104,'abin','j',24)
emp4.printvalue()
emp5=Company()
emp5.setvalue(105,'manu','s',29)
emp5.printvalue()