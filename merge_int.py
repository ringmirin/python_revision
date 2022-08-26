# Input: arr1= [1,2,3,0,0,0], m= 3,arr2=[2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] .

# You are given two integer arrays arr1 and arr2 which are sorted in a non-decreasing order and there are two numbers 
# m and n which represent the number of elements in arr1 and arr2 respectively.

# def fun(arr1):
#    count=0
#    for i in arr1:
#       if arr1[i]>0:
#          count+=1
#    return count
# print(fun([1,2,3,0,0,0]))

def count_by(x, n):
   list=[]
   i=1
   while i<=n:
      a=i*x
      list.append(a)
      i+=1
   return list
print(count_by(2,10))