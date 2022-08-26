# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 
# 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

def sum_count(arr):
   if len(arr)==0:
      return []
   count=sum([1 for i in arr if i>0])
   n=sum([i for i in arr if i<0])
   return [count,n]
print(sum_count([1,2,3,4,-2,-3,-5]))


#####
def sum_count(arr):
   negative=0
   positive=0
   if len(arr)==0:
      return []
   for i in arr:
      if i>0:
         positive+=1
      elif i<0:
         negative+=i
   return [positive,negative]
print(sum_count([1,2,3,4,-3,-2,-4]))

