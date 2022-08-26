def miniMaxSum(arr):
   sort=sorted(arr)
   min=0
   max=0
   i=0
   while i<len(sort):
      min=sum(sort[:i])
      max=sum(sort[1:])
      i+=1
   print(min)
   print(max)
   # print(max)
miniMaxSum([7,69 ,2 ,221, 8974])