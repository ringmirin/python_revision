# ##Write a Python program to sum all the items in a list.

list1=[23,5,6,12,9,7,5,21]
i=0
sum=0
while i<len(list1):
   sum=sum+list1[i]
   i+=1
print(sum)