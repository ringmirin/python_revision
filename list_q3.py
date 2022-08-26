####Write a Python program to get the largest and samllest number from a list.

list1=[2,3,44,77,12,23,56,21,11]
i=0
large=list1[0]
small=list1[0]
while i<len(list1):
   if list1[i]>large:
      large=list1[i]
   if list1[i]<small:
      small=list1
   i+=1
print(large)
print(small)

      