# ##for loops

a=[[4,2,1],[3,2,6],[9,8]]
#O/P=[1,6,8]
list=[]
i=0
while i<len(a):
   j=0
   while i<len(a):
      n=a[i][-1:]
      list+=n
      i+=1
      j+=1
print(list)




# ##  while loops
a=[[4,2,1],[3,2,6],[9,8]]
#O/P=[1,6,8]
list=[]
for i in range(len(a)):
   for j in range(len(a)):
      n=a[i][-1:]
      list+=n
      break
print(list)