# 1 to 1000 list
# lst=[i for i in range(1,1001)]
# print(lst)


# 1. find all of the no from 1 to 1000 that are divisible by 8
# lst1=[i for i in range(1,1001) if(i%8==0)]
# print(lst1)


# 2. find all of the no from 1 to 1000 that have 6 in them
lst=[i for i in range(1,1001) if '6' in  str(i)]
print(lst)


# 3. count no of spaces in a string
# string='practice problems to drill list comprehension problem in your head'
# k=" "
# lst1=[i for i in string if i in k]
# print(len(lst1))
# or
# lst=[i for i in string if i==" "]
# print(len(lst))



# 4. no of vowels in a string count
string='practice problems to drill list comprehension problem in your head'
vowels='aeiouAEIOU'
lst=len([i for i in string if i in vowels])
print(lst)


# 5. find all of the words in a string that are less than 5 letters
string='practice problems to drill list comprehension problem in your head'
lst=[i for i in string.split(' ') if len(i)<5]   #data=string.split(' ')
print(lst)
  
