####output=[1,2,3,4,6,7,8,9]
list=[[1,4,2],[7,3,8],[2,9,4],[2,6]]
i=0
list1=[]
list2=[]
while i<len(list):
   j=0
   while j<len(list[i]):
      a=list[i][j]
      list1.append(a)
      j+=1
   i+=1
for k in list1:
   if k not in list2:
      list2.append(k)
print(list2)    
x=0
while x<len(list2):
   y=x+1
   while y<len(list2):
      if list2[x]>list2[y]:
         a=list2[x]
         list2[x]=list2[y]
         list2[y]=a
      y+=1
   x+=1
print(list2)

