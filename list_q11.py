### Write a Python program to print the numbers of a specified list after removing even 
### numbers from it.

list1=[11,22,33,44,55,66,71,82]
for x in list1:
   if (x%2==0):
      list1.remove(x)
print(list1)


########
i=0
while i<len(list1):
   if (list1[i]%2==0):
      list1.remove(list1[i])
   i+=1
print(list1)
