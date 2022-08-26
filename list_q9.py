# ## Write a Python program to clone or copy a list.

list1=[1,2,3,4,5,12]

list2=list1[:]
print(list2)


######
list2=[]
list2.extend(list1)
print(list2)


