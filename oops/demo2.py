class Person:
    def setvalue(self,fname,lname,age,prof,location):
        self.fname=fname
        self.lname=lname           #instance variables
        self.age=age
        self.prof=prof
        self.location=location
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.prof,self.location)
person1=Person()
person1.setvalue('vinay','vijay',29,'bigdata','kollam')
person1.printvalue()
print('*'*50)
person2=Person()
person2.setvalue('abhi','arun',22,'datascientist','trivandrum')
person2.printvalue()
print('*'*50)
person3=Person()
person3.setvalue('Renjini','Rajeev',23,'datascientist','ernakulam')
person3.printvalue()
print('*'*50)
person4=Person()
person4.setvalue('manu','mohan',19,'tester','allepy')
person4.printvalue()
print('*'*50)
person5=Person()
person5.setvalue('ravi','ram',30,'develepor','kochi')
person5.printvalue()