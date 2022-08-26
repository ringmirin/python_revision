def rotateLeft(d, arr):
   i=0
   temp=[]  
   while i<d:
      temp.append(arr[i])    
      i+=1
   # return temp
   i=0
   while d<len(arr):
      arr[i]=arr[d] 
      i+=1
      d+=1
   arr[:]=arr[:i]+temp
   return arr
print(rotateLeft(2,[1,2,3,4,5]))