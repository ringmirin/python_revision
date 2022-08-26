### Merge two list in ascending order without using any method
def merge_arrays(arr1, arr2):
   arr=[]
   i=0
   temp=0
   while i<len(arr1) and i<len(arr2):
      m=arr1+arr2
      for i in m:
         if i not in arr:
            arr.append(i)
         i+=1
   k=0
   while k<len(arr):
      j=k+1
      while j<len(arr):
         if arr[k]>arr[j]:
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
         j+=1
      k+=1
   return arr
print(merge_arrays([1,8,3,1],[4,9,6,7]))