# create a list which have greater len than the given list
n=["rose","jack","ringmi","ram"]
i=0
list1=[]
while i<len(n):
   if len(n[i])>len(n):
      list1.append(n[i])
   i+=1
print(list1)




