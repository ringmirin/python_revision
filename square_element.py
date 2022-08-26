###Write a Python program to generate and print a list except for the first 5 elements, 
# where the values are square of numbers between 1 and 30 (both included)

i=0
list=[]
while i<=30:
   list.append(i**2)
   i+=1
print(list[5:])

