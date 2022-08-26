####output=[(2,1),(1,2),(2,3),(4,4),(2,5)]

a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
i=0
while i<len(a):
   j=0
   while j<len(a)-1:
      if a[j][1]>a[j+1][1]:
         t=a[j]
         a[j]=a[j+1]
         a[j+1]=t
      j+=1
   i+=1
print(a)


