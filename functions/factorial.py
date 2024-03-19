#factorial of a number


#method 1

def fact():
    num=int(input("enter a number:"))
    i=1
    factorial=1
    while(i<=num):
        factorial*=i
        i+=1               # i is not need in for loop
    print(factorial)
fact()



#method 2
def fact(num):
    i=1
    factorial=1
    while(i<=num):
        factorial*=i
        i+=1
    print(factorial)
fact(5)


# method 3

def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial
data=fact(5)
print(data)
