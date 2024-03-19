# constructor
# ----------------
# replace the method ie; value reading method
# while using constructor instead of method we can pass values while creating objects

#person id fname lname age

class Person():
    def __init__(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age)
per1=Person(101,'ram','r',36)
per1.printvalue()
per2=Person(102,'ravi','e',56)
per2.printvalue()
per3=Person(103,'manu','s',25)
per3.printvalue()
per4=Person(104,'abi','a',28)
per4.printvalue()
per5=Person(105,'hari','s',30)
per5.printvalue()