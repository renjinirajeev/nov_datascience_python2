# map     filter

# map
# if we need a new output for each element in the list we use map function
# [1,2,3,4,5,6,7,8,9,10]  --->  [1,4,9,.....100]

# lst=[1,2,3,4,5,6,7,8,9,10]
# lst1=[]
# for i in lst:
#     lst1.append(i**2)
# print(lst1)



# filter
# used to collect elements from the list within a given condition
# [1,2,3,4,5,6,7,8,9,10]  ---->  [1,3,5,7,9]



# add bonus to all employees ---> map function
# add bonus to all employess if they have 5 yr exp ---> both map and filter
# filter for collecting all employees with 5 yr exp
# map for adding bonus to these emp


# syntax

# variable_name=list(map(function,iterable))
# function written for the task
# iterable ---> list name

# variable_name=list(filter(function,iterable))


lst=[1,2,3,4,5,6,7,8,9,10]
def square(num):
    return num**2
lst1=list(map(square,lst))
print(lst1)



# using lambda function
lst=[1,2,3,4,5,6,7,8,9,10]
f=lambda num:num**2
lst1=list(map(f,lst))
print(lst1)

# or

lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(map(lambda num:num**2,lst))
print(lst1)




lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(filter(lambda num:num%2==0,lst))
print(lst1)

print("_"*100)


lst=[1,2,3,4,5,6,7,8,9]
lst1=list(map(lambda num:num**2,lst))
lst2=list(filter(lambda  num:num%2!=0,lst1))
print(lst2)


