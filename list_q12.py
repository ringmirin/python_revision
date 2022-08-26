### Write a Python program to generate and print a list of first and last 5 elements 
### where the values are square of numbers between 1 and 30 (both included).


list1=[]
for i in range(1,30+1):
   list1.append(i**2)
# print(list1)
a=list1[:5]
b=list1[-5:]
print(a)
print(b)


#########
i=0
list=[]
while i<=30:
   list.append(i**2)
   i+=1
print(list[:5])
print(list[-5:])





