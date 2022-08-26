# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.


def sum_mix(arr):
   sum=0
   for i in arr:
      a=int(i)
      sum+=a 
   return sum
print(sum_mix(["2","3",4,5]))
   
   



