#student
#id,fname,lname,age,course,location
# 5object
class Student():
    college_name='MES'          # static variable
    def setvalue(self,id,fname,lname,age,course,location):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.location=location
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.course,self.location,Student.college_name)
stud1=Student()
stud1.setvalue(101,'Abhishek','abhi',22,'testing','tvr')
stud1.printvalue()
print('*'*100)
stud2=Student()
stud2.setvalue(102,'Ram','rahul',34,'datascience','kollam')
stud2.printvalue()
print('*'*100)
stud3=Student()
stud3.setvalue(103,'Renji','ram',29,'MERN','alp')
stud3.printvalue()
print('*'*100)
stud4=Student()
stud4.setvalue(104,'Renjini','rs',39,'MEAN','calicut')
stud4.printvalue()
print('*'*100)
stud5=Student()
stud5.setvalue(105,'Amal','M',29,'bigdata','wayand')
stud5.printvalue()
print('*'*100)
stud6=Student()
stud6.setvalue(106,'Reshma','Rajeev',18,'science','kannur')
stud6.printvalue()

#instance variable
#static variable       common value(college name)