# ###Write a Python program to multiply all the items in a list.

list1=[2,4,6,8,11,7,9,8]
i=0
mult=1
while i<len(list1):
   mult=mult*list1[i]
   i+=1
print(mult)