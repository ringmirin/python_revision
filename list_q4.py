### Write a Python program to count the number of strings where the string length is 2 
### or more and the first and last character are same from a given list of strings.

sample_list= ['abc', 'xyz', 'aba', '1221']
i=0
count=0
while i<len(sample_list):
   j=0
   while j<len(sample_list[i]):
      if sample_list[i][0]==sample_list[i][-1]:      
         count+=1
         break
      j+=1
   i+=1
print(count)