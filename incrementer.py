# Given an input of an array of digits, return the array with each digit incremented by its position in the array: the first 
# digit will be incremented by 1, the second digit by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).

def incrementor(nums):
   list=[]
   i=0
   j=1
   while i<len(nums):
      a=nums[i]+j
      list.append(a)
      if list[i]>9:
         list[i]=list[i]%10
      i+=1
      j+=1
   return list
print(incrementor([5, 8, 2, 5, 8]))
      