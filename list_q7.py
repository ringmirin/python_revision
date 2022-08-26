### Write a Python program to remove duplicates from a list.
list1=[2,5,3,7,9,1,5,2,4,6,3]
list2=[]
i=0
while i<len(list1):
   for n in list1:
      if n not in list2:
         list2.append(n)
      i+=1
print(list2)

