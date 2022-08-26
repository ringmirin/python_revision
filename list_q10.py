### Write a Python program to find the list of words that are longer than n from a given 
### list of words.

list1=["ringmirin","wonnao","worin","chun","ato"]
i=0
list2=[]
while i<len(list1):
   if len(list1[i])>5:
      list2.append(list1[i])
   i+=1
print(list2)


####
i=0
count=0
while i<len(list1):
   if len(list1[i])>5:
      count+=1
   i+=1
print(count)