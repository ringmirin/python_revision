### Given an array of integers. Find the minimum sum which is obtained from summing each Two integers product.

def min_sum(arr):
   i=0
   sum=0
   sort_list=[]
   rev_list=[] 
   sort=sorted(arr)
   rev=sorted(arr,reverse=True)
   rng=len(arr)/2
   for i in range(0,int(rng)):
      sort_list.append(sort[i])
      rev_list.append(rev[i])
   for x in range(len(sort_list)):
      sum+=rev_list[x]*sort_list[x]
   return sum
print(min_sum([12,6,10,26,3,24]))





