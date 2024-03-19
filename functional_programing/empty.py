# empty list
# 1 to 30
# odd n0s
# square of that odd nos


lst1=[]
for i in range(1,31):
     lst1.append(i)
print(lst1)
lst2=list(filter(lambda num:num%2==1,lst1))
print(lst2)
lst3=list(map(lambda num:num**2,lst2))
print(lst3)