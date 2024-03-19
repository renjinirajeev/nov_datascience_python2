# method 3


# 3.     syntax (Range of elements list based on more than 1 condition)

# lst=[print1 if condition1 else print2 range]
# print(lst)
# even ---> square , odd  ----> cube

# we cannot apply elif instead can use multiple if else
# lst=[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range ]


# 1 to 50 range even no square odd cube
lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,51)]
print(lst)


# 1 to 50 range
# 1 to 15 ---> small
# 16 to 35 ---> medium
# 36 ---> large
# lst=[(i,'small')if i<=15 else (i,"medium") if 16<=i<=35 else (i,"large") for i in range(1,51)]
# print(lst)


# 1 to 1000 list

# 1. find all of the no from 1 to 1000 that are divisible by 8
# 2. find all of the no from 1 to 1000 that have 6 in them
# 3. count no of spaces in a string
# 4. no of vowels in a string count
# 5. find all of the words in a string that are less than 5 letters
# string='practice problems to drill list comprehension problem in your head'


