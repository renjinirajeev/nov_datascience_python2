# #create a simple calculator using function
#
#
# def cal():
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Multiplication")
#     print("4. Division")
#     i=int(input("Enter your choice:"))
#     if(i==1):
#         def add():
#            num1 = int(input("enter number1:"))
#            num2 = int(input("enter number2:"))
#            sum=num1+num2
#            return sum
#         add()
#     elif(i==2):
#         def sub():
#             num1 = int(input("enter number1:"))
#             num2 = int(input("enter number2:"))
#             dif=num1-num2
#             return dif
#         data1= sub(5, 7)
#         print(data1)
#     elif(i==3):
#         def multi(num1, num2):
#             mul=num1*num2
#             return mul
#         data2 = multi(5, 7)
#         print(data2)
#     elif(i==4):
#         def divi (num1, num2):
#             div=num1/num2
#             return div
#         data3= divi(5, 7)
#         print(data3)
#     else:
#         def msg(mes):
#             mes='invalid choice'
#             return mes
#         data4 = msg('invalid choice')
#         print(data4)
# cal(1,5)



def add(num1,num2):
    res=num1+num2
    return res
def sub(num1,num2):
    res=num1-num2
    return res
def mul(num1,num2):
    res=num1*num2
    return res
def div(num1,num2):
    res=num1/num2
    return res

print("1. Addition\n"
      "2. Substraction\n"
      "3. Multiplication\n"
      "4. Division")

choice=int(input("Enter Your Choice:"))
if(choice==1):
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    print(num1,"+",num1,"=",add(num1,num2))
elif(choice==2):
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    print(num1, "-", num1, "=", sub(num1, num2))
elif(choice==3):
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    print(num1, "*", num1, "=", mul(num1, num2))
elif(choice==4):
    num1 = int(input("enter number 1:"))
    num2 = int(input("enter number 2:"))
    print(num1, "/", num1, "=", div(num1, num2))
else:
    print("Invalid Choice")


