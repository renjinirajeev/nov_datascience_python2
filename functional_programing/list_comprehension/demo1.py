

#list comprehension


# single line
# only 1 syntax
# 3 methods

#1. Range of elements added into a list

#2. Range of elemnts added into a list based on one condition

#3. Range of elemets added into a list based on more than 1 condition


# 1.     syntax
# lst=[print range]

lst=[i for i in range (1,31)]
print(lst)


# 1 to 25
# lst=[i for i in range(1,26)]
# print(lst)


# 1 to 10 range square
# lst=[i**2 for i in range(1,11)]
# print(lst)



# add 5 to each elements in the lst
# lst=[1,2,3,4,5]
# lst1=[i+5 for i in lst]
# print(lst1)




# 2.     syntax (Range of elements list based on 1 condition)

# lst=[print range if condition]
# print(lst)


# 1 to 20 even number
# lst=[i for i in range(1,21) if(i%2==0)]
# print(lst)


# 1 to 30 range divisible by 5
# lst=[i for i in range(1,31) if i%5==0]
# print(lst)

# 1 to 40 odd no square
# lst=[(i,i**2) for i in range(1,41) if(i%2==1)]
# print(lst)






# 3.     syntax (Range of elements list based on more than 1 condition)

# lst=[print1 if condition1 else print2 range]
# print(lst)
# even ---> square , odd  ----> cube
# we cannot apply elif instead can use multiple if else
# lst=[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range ]



# 1 to 50 range even no square odd cube
lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,51)]
print(lst)